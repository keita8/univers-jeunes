from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.db.models import Count, Q
from .models import Post
from marketing.models import SignUp
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .forms import CommentForm
# Create your views here.


def search(request):

    queryset = Post.objects.all()
    query = request.GET.get('q')
    queryset_count = 0

    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) | 
            Q(overview__icontains=query)  
        ).distinct()

        queryset_count = queryset.filter(

            Q(title__icontains=query) | Q(overview__icontains=query)

            ).distinct().values('title').annotate(Count('title'))

    print(queryset_count.count())

    context = {

        'queryset' : queryset,


    }

    return render(request, 'layouts/search_result.html', context)


def get_category_count():
    queryset = Post.objects.values('categories__title').annotate(Count('categories__title'))
    return queryset

    
# fonction dediée à la page d'accueil
def home(request):

    queryset      = Post.objects.all().filter(featured=True)
    last_post     = Post.objects.order_by('-timestamp')[:3]

    if request.method == 'POST':
        sender           = request.POST['email']
        new_signup       = SignUp()
        new_signup.email = sender
        new_signup.save()

    context = {

        'queryset'      : queryset,
        'last_post'     : last_post,
    }

    return render(request, 'index.html', context)


# --------------------------------------------------------------------------------------------------------
# fonction dediée à la partie blog
def blog(request):

    category_count = get_category_count()
    most_recent    = Post.objects.order_by('-timestamp')[:3]
    article_list   = Post.objects.all()
    paginator      = Paginator(article_list, 4)
    page_request   = 'page'
    page           = request.GET.get(page_request)

    # print(category_count)
    try:
        paginator_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginator_queryset = paginator.page(1)
    except EmptyPage:
        paginator_queryset = paginator.page(paginator.num_pages)

    context = {
        'queryset': paginator_queryset,
        'page_request': page_request,
        'most_recent' : most_recent,
        'category_count' : category_count,
    }
    return render(request, 'layouts/blog.html', context)



# --------------------------------------------------------------------------------------------------------
# fonction dediée à un article du blog
def post(request, id):

    category_count = get_category_count()
    most_recent    = Post.objects.order_by('-timestamp')[:3]
    post = get_object_or_404(Post, id=id)


    # if request.user.is_authenticated:
    #     PostView.objects.get_or_create(user=request.user, post=post)

    form = CommentForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            # form.instance.post = request.post
            form.save()
            return redirect(reverse("post", kwargs={
                'id': post.pk
            }))

    context = {

        'post'           : post,
        'category_count' : category_count,
        'most_recent'    : most_recent,
        'form'           : form,
    }

    return render(request, 'layouts/post.html', context)
