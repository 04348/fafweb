from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

def home(request):
    if "https" in request.build_absolute_uri():
        redirect(request.build_absolute_uri().replace('https', 'http'))
    return render(request, 'home.html')

def redir(request, url):
    return redirect(url)
