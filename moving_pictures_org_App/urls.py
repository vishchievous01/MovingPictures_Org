from django.urls import path
from moving_pictures_org.urls import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('welcome/', views.welcome, name="welcome"),
    path('errorPage/', views.errorPage, name="errorPage"),
    path('blogDetail/', views.blogDetail, name="blogDetail"),
    path('blogGrid/', views.blogGrid, name="blogGrid"),
    path('blogList.', views.blogList, name="blogList"),
    path('celebrityGrid01/', views.celebrityGrid01, name="celebrityGrid01"),
    path('celebrityGrid02/', views.celebrityGrid02, name="celebrityGrid02"),
    path('celebrityList/', views.celebrityList, name="celebrityList"),
    path('celebritySingle/', views.celebritySingle, name="celebritySingle"),
    path('comingSoon/', views.comingSoon, name="comingSoon"),
    path('homeV2/', views.homeV2, name="homeV2"),
    path('homeV3/', views.homeV3, name="homeV3"),
    path('movieGrid/', views.movieGrid, name="movieGrid"),
    path('movieGridFW/', views.movieGridFW, name="movieGridFW"),
    path('movieList/', views.movieList, name="movieList"),
    path('movieSingle/', views.movieSingle, name="movieSingle"),
    path('seriesSingle/', views.seriesSingle, name="seriesSingle"),
    path('userFavoriteGrid/', views.userFavoriteGrid, name="userFavoriteGrid"),
    path('userProfile/', views.userProfile, name="userProfile"),
    path('userRate/', views.userRate, name="userRate"),
]
