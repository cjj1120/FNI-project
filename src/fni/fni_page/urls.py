from django.urls import path
from . import views
#from django.conf.urls import url    
from django.urls import re_path as url

app_name = 'fni_page'

urlpatterns = [
    path('', views.home, name="home"),
    path('inflation', views.inflation, name = "inflation"),  
    path('about', views.about, name = "about"), 
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    path('insert_trend_data', views.insert_trend_data, name='insert_trend_data'),
]