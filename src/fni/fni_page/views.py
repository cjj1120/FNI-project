from django.shortcuts import render
from django.http import HttpResponse



def home(request):
	return render(request, 'fni_page/home.html')

def inflation(request):
	return render(request, 'fni_page/inflation.html')

def about(request):
	return render(request, 'fni_page/about.html')


