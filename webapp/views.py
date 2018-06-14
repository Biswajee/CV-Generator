from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'webpages/index.html')


def signup(request):
    return render(request, 'webpages/signup.html')


def signin(request):
    return render(request, 'webpages/signin.html')


def formfill(request):
    return render(request, 'webpages/fillform.html')

def profile(request):

    return render(request, 'webpages/signin.html')

def read_docs(request):
    return render(request, 'webpages/read_docs.html')
