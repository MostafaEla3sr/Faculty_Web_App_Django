from datetime import date, datetime
from email.mime import image
from email.policy import default
from re import T
from tabnanny import verbose
from django.db import models
from datetime import datetime

# Create your models here.
    
class student (models.Model):
    choices = [("CS" , "CS"),("IS" , "IS"),("IT" , "IT")]
    f_name = models.CharField(max_length=20 , null = True , verbose_name="First Name" )
    l_name = models.CharField(max_length=20 , null = True , verbose_name="Last Name" )
    address = models.CharField(max_length=50 , default="Menofia" , verbose_name="Address" )
    specialization = models.CharField( max_length=50 , choices=choices , null = True )
    birthDate = models.DateField(null = True , verbose_name="Birthday")
    image = models.ImageField(upload_to='photos/%y/%m/%d' , default= 'photos/22/09/20/img2.jpg')
    def __str__ (self):
        return self.f_name

class doctor (models.Model):
    f_name = models.CharField(max_length=20 , null = True , verbose_name="First Name" )
    l_name = models.CharField(max_length=20  , null = True, verbose_name="Last Name" )
    address = models.CharField(max_length=50 , null = True , default="Menofia" , verbose_name="Address")
    birthDate = models.DateField(null = True , verbose_name="Birthday")
    image = models.ImageField(upload_to='photos/%y/%m/%d' , default= 'photos/22/09/20/img2.jpg')
    def __str__ (self):
        return self.f_name

class TeachingAssistant(models.Model):
    f_name = models.CharField(max_length=20 , null = True , verbose_name="First Name" )
    l_name = models.CharField(max_length=20 , null = True , verbose_name="Last Name" )
    address = models.CharField(max_length=50 , null = True , default="Menofia" , verbose_name="Address")
    birthDate = models.DateField(null = True , verbose_name="Birthday")
    image = models.ImageField(upload_to='photos/%y/%m/%d' , default= 'photos/22/09/20/img2.jpg')
    def __str__ (self):
        return self.f_name

class subject (models.Model):
    name = models.CharField(max_length=30 , null = True , verbose_name="Subject Name")
    hours = models.IntegerField(default=3 , verbose_name="Subject hours")
    def __str__ (self):
        return self.name

