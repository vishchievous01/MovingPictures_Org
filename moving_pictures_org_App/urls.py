from django.urls import path
from moving_pictures_org.urls import views


urlpatterns = [
    path('welcome/', views.welcome, name="welcome"),
    path('error_page/', views.error_page, name="error_page"),
]
