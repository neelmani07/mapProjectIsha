from tkinter import CASCADE
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from phonenumber_field.modelfields import PhoneNumberField


class User(models.Model):
    name = models.CharField(max_length=100)
    contact_no = PhoneNumberField()
    email_id = models.EmailField(max_length=250)
    profile_pic = models.ImageField(null=True)
    profile_status = models.TextField()
    is_special_entity = models.BooleanField(null=False)

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    location = Point()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

class LoginCredentials(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    user_password = models.CharField(max_length=100)

class Role(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    role_type = models.CharField( max_length=50)

class Features(models.Model):
    role = models.ForeignKey(Role, on_delete=CASCADE)
    action = models.CharField(max_length=100)