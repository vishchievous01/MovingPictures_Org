from django.urls import path
from moving_pictures_org.urls import views


urlpatterns = [
    path('welcome/', views.welcome, name="welcome"),
    path('errorPage/', views.errorPage, name="errorPage"),
    path('blogDetail/', views.blogDetail, name="blogDetail"),
]
