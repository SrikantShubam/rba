from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=100, blank=False)
    age = models.PositiveIntegerField(null=True, blank=True)
     


class data_collected(models.Model):
    Uid=models.CharField(max_length=400,default="Id not given")
    userid=models.CharField(max_length=400,null=True,blank=True,default="something")
    ip=models.CharField(max_length=40,null=True,blank=True,default="something")
    date=models.DateField()
    time_zone=models.CharField(max_length=40,default='UTC',null=True,blank=True)
    language=models.CharField(max_length=40,default='en-US',null=True,blank=True)
    system_fonts=models.CharField(max_length=10000,default='Arial',null=True,blank=True)
    # browser_fonts=models.CharField(max_length=200,default='Arial',null=True,blank=True)
    time_collected=models.TimeField(default=0)
    city=models.CharField(max_length=20,default='SOME STRING',null=True,blank=True)
    region=models.CharField(max_length=20,default='SOME STRING',null=True, blank=True)
    country=models.CharField(max_length=40,default='SOME STRING',null=True, blank=True)
    browser_name = models.CharField(max_length=400,default='Something')
    browser_version = models.CharField(max_length=400,default='Something')
    os_family = models.CharField(max_length=400,default="something")
    os_version = models.CharField(max_length=400,default='Something')
    screensize=models.CharField(max_length=20,default=0)
    # plugins=models.CharField(max_length=200,default='Something',null=True,blank=True)
    # canvas=models.CharField(max_length=200,default="null",null=True,blank=True)
    # webgl=models.CharField(max_length=200,default="null",null=True,blank=True)
    ua_totaltime=models.CharField(max_length=200,default=0,blank=True,null=True)
    ip_totaltime=models.CharField(max_length=200,default=0,blank=True,null=True)
    timezone_totaltime=models.CharField(max_length=200,default=0,blank=True,null=True)
    location_totaltime=models.CharField(max_length=200,default=0,blank=True,null=True)
    screensize_totaltime=models.CharField(max_length=200,default=0,blank=True,null=True)
    system_fonts_totaltime=models.CharField(max_length=200,default=0,blank=True,null=True)
    browser_fonts_totaltime=models.CharField(max_length=200,default=0,blank=True,null=True)
    # plugins_totaltime=models.CharField(max_length=200,default=0,blank=True,null=True)
    # canvas_totaltime=models.CharField(max_length=200,default=0,blank=True,null=True)
    # webgl_totaltime=models.CharField(max_length=200,default=0,blank=True,null=True)
    lang_totaltime=models.CharField(max_length=200,default=0,blank=True,null=True)
    overall_totaltime=models.CharField(max_length=200,default=0,blank=True,null=True)