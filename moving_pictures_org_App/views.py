from django.shortcuts import render, redirect
from django.http import HttpResponse


def welcome(request):
    return render(request, "landing.html")


def errorPage(request):
    return render(request, "404.html")


def blogDetail(request):
    theme = request.GET.get('theme', 'dark')
    if theme == 'light':
        return render(request, "blogdetail_light.html")
    return render(request, "blogdetail.html")
