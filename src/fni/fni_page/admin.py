from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Trend)
admin.site.register(User_profile)