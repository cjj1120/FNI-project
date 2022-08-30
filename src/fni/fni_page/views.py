from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import * 
from .forms import * 
from pytrends.request import TrendReq
from datetime import datetime, timedelta

def home(request):
	return render(request, 'fni_page/home.html')

@login_required(login_url='/user_login')
def inflation(request):
    trends = Trend.objects.order_by('-data_created')[:5]
    return render(request, 'fni_page/inflation.html', {'trend_list': trends})

def about(request):
	return render(request, 'fni_page/about.html')

def insert_trend_data(request):
    pytrend = TrendReq()
    today_date = str(datetime.datetime.now().date())
    ystd = str((datetime.today() - timedelta(days=1)).date())
    pytrend.build_payload(kw_list=['Inflation'],timeframe=f'{ystd} {today_date}')
    related_queries = pytrend.related_queries()['Inflation']['top'].head()
    for i,row in related_queries.iterrows():
        data_ = Trend(query_res=row['query'], value=row['value'])
        data_.save()
    return HttpResponseRedirect('/inflation')


# Login views: 
def index(request):
    return render(request, 'fni_page/home.html')

@login_required
def special(request):
    all_users = User_profile.objects.select_related('user')
    return HttpResponse(all_users[0].occupation_and_monthly_saving)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('/home'))

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user=user
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else: # if GET request
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    
    return render(request,'fni_page/registration.html',
    {'user_form':user_form,
    'profile_form':profile_form,
    'registered':registered}
    )

def user_login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/inflation')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request,'fni_page/login.html')
