from django.db import models
from actstream import registry

# Create your models here.


class Blog(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    text = models.TextField()
    pub_date = models.DateTimeField()



#registry.register(Blog)
