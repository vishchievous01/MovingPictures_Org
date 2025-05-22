from django.contrib import admin
from django.urls import path, include
from moving_pictures_org_App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('moving_pictures_org_App.urls'))
]
