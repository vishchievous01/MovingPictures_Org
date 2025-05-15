from django.shortcuts import render, redirect
from django.http import HttpResponse

def welcome(request):
    return render(request, "landing.html")

def error_page(request):
    return render(request, "404.html")