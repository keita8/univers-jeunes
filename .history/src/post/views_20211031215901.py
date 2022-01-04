from django.shortcuts import render

# Create your views here.

# fonction dediée à la page d'accueil


def home(request):
    context = {}
    return render(request, 'index.html', context)


# fonction dediée à la partie blog
def blog(request):
    context = {}
    return render(request, 'layouts/blog.html', context)


# fonction dediée à un article du blog
def post(request):
    context = {}
    return render(request, 'layouts/post.html', context)
