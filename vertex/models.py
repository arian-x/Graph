from django.db import models
import datetime
from django.utils import timezone

class Vertex(models.Model,object):
    name = models.CharField(max_length=200)
    reg_date = models.DateTimeField('date published')
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name
    def __init__(self,info_dict)
    	pass
        
# Create your models here.
