from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def view_buildSelect(request):
    return render(request, 'build/buildSelect.html')

def view_build(request, prof):
    return render(request, 'build/build.html', {'prof': prof})