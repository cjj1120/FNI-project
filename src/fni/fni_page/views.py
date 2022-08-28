from django.shortcuts import render
from django.http import HttpResponse
from .models import * 


def home(request):
	return render(request, 'fni_page/home.html')

def inflation(request):
    trends = Trend.objects.order_by('-data_created')[:5]
    return render(request, 'fni_page/inflation.html', {'trend_list': trends})

def about(request):
	return render(request, 'fni_page/about.html')


