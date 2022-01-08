from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.admin.views.decorators import staff_member_required
from .models import Post, Category, Author, PostView
from marketing.models import SignUp
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .forms import CommentForm, PostForm, ContactForm
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from django.http import Http404
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from marketing.forms import EmailSignupForm
from marketing.views import subscription

form = EmailSignupForm()
#----------------------------------------------------------------------------------------------#
# RECUPERER UN EDITEUR
def get_author(user):
    queryset = Author.objects.filter(user=user)

    if queryset.exists():
        return queryset[0]
    return None

#----------------------------------------------------------------------------------------------#
# FONCTION DE RECHERCHE


def search(request):
    queryset = Post.objects.filter(status='publie')
    query = request.GET.get('q')
    category_count = get_category_count()

    # post_list = Post.objects.all()
    # most_recent = Post.objects.order_by('-timestamp')[:4]
    # paginator = Paginator(queryset, 4)
    # page_request_var = 'page'
    # page = request.GET.get(page_request_var)

    # try:
    # 	paginated_queryset = paginator.page(page)
    # except PageNotAnInteger:
    # 	paginated_queryset = paginator.page(1)
    # except EmptyPage:
    # 	paginated_queryset = paginator.page(paginator.num_pages)

    if query:

        queryset = queryset.filter(

            Q(title__icontains=query) |
            Q(overview__icontains=query) | Q(content__icontains=query)
        ).distinct()

    # paginator = Paginator(queryset, 4)
    # page_request_var = 'page'
    # page = request.GET.get(page_request_var)

    # try:
    # 	paginated_queryset = paginator.page(page)
    # except PageNotAnInteger:
    # 	paginated_queryset = paginator.page(1)
    # except EmptyPage:
    # 	paginated_queryset = paginator.page(paginator.num_pages)

    context = {

        'queryset': queryset,
        # 'page_request_var' : page_request_var,
        # 'most_recent'      : most_recent,
        # 'category_count'   : category_count
    }

    return render(request, 'search_results.html', context)

#----------------------------------------------------------------------------------------------#
# RECUPERER LE NOMBRE D'ARTICLE ASSOCIE A UNE CATEGORIE


def get_category_count():
    queryset = Post.objects.values(
        'categories__title').annotate(Count('categories__title'))
    return queryset

#----------------------------------------------------------------------------------------------#
# PAGE D'ACCUEIL

def index(request):
    queryset = Post.objects.filter(status='publie').order_by('-timestamp')
    latest = Post.objects.filter(status='publie').order_by('-timestamp')[0:3]

    if request.method == "POST":
        email = request.POST['email']
        new_signup = SignUp()
        # subscription(email)
        new_signup.email = email
        messages.success(request, 'Merci d\'avoir souscrit à la newsletter')
        new_signup.save()

    context = {

        'queryset': queryset,
        'latested': latest,
    }
    return render(request, 'index.html', context)

#----------------------------------------------------------------------------------------------#
# PAGE DU BLOG (ARTICLES)

def blog(request):


    category_count = get_category_count()
    post_list = Post.objects.filter(status='publie')

    most_recent = Post.objects.order_by('-timestamp')[:4]
    per_page = 4
    paginator = Paginator(post_list, per_page)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
        'most_recent': most_recent,
        'category_count': category_count,
        'per_page': per_page
    }
    return render(request, 'blog.html', context)

#----------------------------------------------------------------------------------------------#
# DETAILS SUR UN ARTICLE PARTICULIER

def post(request, slug):

    post = get_object_or_404(Post, slug=slug)
    most_recent = Post.objects.order_by('-timestamp')[:4]
    category_count = get_category_count()
    value = "Il y a"

    if request.user.is_authenticated:
        PostView.objects.get_or_create(user=request.user, post=post)

    form = CommentForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect(reverse('post', kwargs={'slug': post.slug}))

    context = {
        'form': form,
        'post': post,
        # 'page_request_var' : page_request_var,
        'most_recent': most_recent,
        'category_count': category_count,
        'value' : value,
    }

    return render(request, 'post.html', context)

#----------------------------------------------------------------------------------------------#
# REDIGER UN NOUVEL ARTICLE
@staff_member_required
def post_create(request):

    titre = "Nouvel article"
    confirmation = "Créer"
    author = get_author(request.user)

    if request.method == 'POST':
        form = PostForm(request.POST or None, request.FILES or None)

        if form.is_valid():

            form.instance.author = author
            form.save()

            return redirect(reverse('post', kwargs={'slug': form.instance.slug}))
    else:
        form = PostForm()

    context = {'form': form, 'titre1': titre, 'titre': confirmation}
    return render(request, 'post_create.html', context)

#-----------------------------------------------------------------------------------------------#
# MODIFIER UN ARTICLE

@staff_member_required
def post_update(request, slug):
    titre = 'Modifier article'
    confirmation = "Modifier"
    post = get_object_or_404(Post, slug=slug)
    form = PostForm(
        request.POST or None,
        request.FILES or None,
        instance=post)
    author = get_author(request.user)

    if post.author == author:
        if request.method == "POST":
            if form.is_valid():
                form.instance.author = author
                form.save()
                return redirect(reverse("post", kwargs={
                    'slug': form.instance.slug
                }))
    else:
        raise Http404

    context = {
        'titre1': titre,
        'titre': confirmation,
        'form': form
    }
    return render(request, "post_create.html", context)

#----------------------------------------------------------------------------------------------#
# SUPPRIMER D'UN ARTICLE

@staff_member_required
def post_delete(request, slug):
    author = get_author(request.user)
    post = Post.objects.get(slug=slug)

    if post.author == author:
        post.delete()
        return redirect('blog')
    else:
        raise Http404


def contact(request):
    form = ContactForm()

    context = {
        'form': form
    }

    return render(request, 'contact.html', context)
