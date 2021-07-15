from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author': 'tiVnqi',
        'title' : 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'July 11, 2021'
    },
    {
        'author': 'Max Mustermann',
        'title' : 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'July 12, 2021'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
