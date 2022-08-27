from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('inflation', views.inflation),  
    path('about', views.about)  
]