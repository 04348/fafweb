from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

def home(request):
    if (request.build_absolute_uri().contains('https')):
        redirect(request.build_absolute_uri().replace('https', 'http'))
    return render(request, 'home.html')

def redir(request, url):
    return redirect(url)
