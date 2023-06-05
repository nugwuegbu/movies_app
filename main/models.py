from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Movies(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    title = models.CharField(null=False,max_length=255,blank=False)
    imdb_id = models.CharField(null=False,max_length=10)
    published_date = models.DateTimeField()
