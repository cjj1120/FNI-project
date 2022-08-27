from django.db import models

# Create your models here.

# query results and value. 
class Trend(models.Model):
    query_res = models.CharField(max_length=200)
    value = models.CharField(max_length=200, null=True)
    data_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.query_res # render Hello on the admin page Under Treend. 