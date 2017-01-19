from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
# Create your views here.

def home(request):
    return render(request, 'home.html')

def redir(request, url):
    return redirect(url)
