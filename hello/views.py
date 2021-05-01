from django.shortcuts import render

def index(request):
    return render(request, 'hello/index.html')

def about(request):
    return render(request, 'hello/about.html')
