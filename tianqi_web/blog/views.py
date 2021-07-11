from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>Blog Home</h1>')


def about(request):
    return HttpResponse('<h2>Blog About</h2>')


def forum(request):
    return HttpResponse('<h2>Blog Forum</h2>')
