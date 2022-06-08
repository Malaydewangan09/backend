from django.db import models
from datetime import datetime
# Create your models here.
class Topic(models.Model):
    
    name = models.CharField(max_length = 50 )
    object = models.TextField(max_length = 500)
    time = models.DateTimeField()
     
    def __str__(self):
        return self.name