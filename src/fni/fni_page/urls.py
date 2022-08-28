from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('inflation', views.inflation, name = "inflation"),  
    path('about', views.about, name = "about")  
]