from django.shortcuts import render

# Create your views here.


def home(request):
    context = {}
    return render(request, 'index.html', context)


def blog(request):
    context = {}
    return render(request, 'layouts/blog.html', context)
