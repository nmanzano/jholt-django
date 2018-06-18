from django.shortcuts import render


def jholtsite(request):
    return render(request, 'enter/enter.html', {})


def home(request):
    return render(request, 'home/home.html', {})


def about(request):
    return render(request, 'about/about.html', {})
