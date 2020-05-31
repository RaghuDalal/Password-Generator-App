from django.contrib import admin
from django.urls import path

from generator import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('password/', views.password, name='password'),
]
