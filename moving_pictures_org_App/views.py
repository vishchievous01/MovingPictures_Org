from django.shortcuts import render, redirect
from django.http import HttpResponse


def index(request):
    theme = request.GET.get('theme', 'dark')
    if theme == 'light':
        return render(request, "index_light.html")
    return render(request, "index.html")


def index2(request):
    return render(request, "index-2.html")


def welcome(request):
    return render(request, "landing.html")


def errorPage(request):
    return render(request, "404.html")


def blogDetail(request):
    theme = request.GET.get('theme', 'dark')
    if theme == 'light':
        return render(request, "blogdetail_light.html")
    return render(request, "blogdetail.html")


def blogGrid(request):
    theme = request.GET.get('theme', 'dark')
    if theme == 'light':
        return render(request, "bloggrid_light.html")
    return render(request, 'bloggrid.html')


def blogList(request):
    theme = request.GET.get('theme', 'dark')
    if theme == 'light':
        return render(request, "bloglist_light.html")
    return render(request, "bloglist.html")


def celebrityGrid01(request):
    theme = request.GET.get('theme', 'dark')
    if theme == 'light':
        return render(request, "celebritygrid01_light.html")
    return render(request, "celebritygrid01.html")


def celebrityGrid02(request):
    theme = request.GET.get('theme', 'dark')
    if theme == 'light':
        return render(request, "celebritygrid02_light.html")
    return render(request, "celebritygrid02.html")


def celebrityList(request):
    theme = request.GET.get('theme', 'dark')
    if theme == 'light':
        return render(request, "celebritylist_light.html")
    return render(request, "celebritylist.html")


def celebritySingle(request):
    theme = request.GET.get('theme', 'dark')
    if theme == 'light':
        return render(request, "celebritysingle_light.html")
    return render(request, "celebritysingle.html")


def comingSoon(request):
    return render(request, "comingsoon.html")


def homeV2(request):
    theme = request.GET.get('theme', 'dark')
    if theme == 'light':
        return render(request, "homev2_light.html")
    return render(request, "homev2.html")


def homeV3(request):
    theme = request.GET.get('theme', 'dark')
    if theme == 'light':
        return render(request, "homev3_light.html")
    return render(request, "homev3.html")


def movieGrid(request):
    theme = request.GET.get('theme', 'dark')
    if theme == 'light':
        return render(request, "moviegrid_light.html")
    return render(request, "moviegrid.html")


def movieGridFW(request):
    theme = request.GET.get('theme', 'dark')
    if theme == 'light':
        return render(request, "moviegridfw_light.html")
    return render(request, "moviegridfw.html")


def movieList(request):
    theme = request.GET.get('theme', 'dark')
    if theme == 'light':
        return render(request, "movielist_light.html")
    return render(request, "movielist.html")


def movieSingle(request):
    theme = request.GET.get('theme', 'dark')
    if theme == 'light':
        return render(request, "moviesingle_light.html")
    return render(request, "moviesingle.html")


def seriesSingle(request):
    theme = request.GET.get('theme', 'dark')
    if theme == 'light':
        return render(request, "seriessingle_light.html")
    return render(request, "seriessingle.html")


def userFavoriteGrid(request):
    theme = request.GET.get('theme', 'dark')
    if theme == 'light':
        return render(request, "userfavoritegrid_light.html")
    return render(request, "userfavoritegrid.html")


def userProfile(request):
    theme = request.GET.get('theme', 'dark')
    if theme == 'light':
        return render(request, "userprofile_light.html")
    return render(request, "userprofile.html")


def userRate(request):
    theme = request.GET.get('theme', 'dark')
    if theme == 'light':
        return render(request, "userrate_light.html")
    return render(request, "userrate.html")
