from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# query results and value. 
class Trend(models.Model):
    query_res = models.CharField(max_length=200)
    value = models.CharField(max_length=200, null=True)
    data_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.query_res # render Hello on the admin page Under Treend. 

class User_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    occupation_and_monthly_saving =models.TextField(blank=True)
    def __str__(self):
        return self.user.username