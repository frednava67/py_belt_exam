# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import messages
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX  = re.compile('[0-9]')

class UserManager(models.Manager):
    def basic_validator(self, newrequest):
        bFlashMessage = False

        f_name = newrequest.POST['first_name']
        l_name = newrequest.POST['last_name']
        email = newrequest.POST['email']
        pwd = newrequest.POST['password']
        confpwd = newrequest.POST['confirmpw']

        # First Name - Required; No fewer than 2 characters; letters only
        if len(f_name) < 2 or NAME_REGEX.search(f_name):
            messages.error(newrequest, u"First Name can only contain letters and be at least 2 characters", extra_tags="fname")
            bFlashMessage = True  

        # Last Name - Required; No fewer than 2 characters; letters only
        if len(l_name) < 2 or NAME_REGEX.search(l_name):
            messages.error(newrequest, u"Last Name can only contain letters and be at least 2 characters", extra_tags="lname")
            bFlashMessage = True     

        # Email - Required; Valid Format
        if not EMAIL_REGEX.match(email):
            messages.error(newrequest, u"Invalid Email Address!", extra_tags="email")
            bFlashMessage = True      

        #Email shouldn't be in database already
        i = User.objects.filter(email=email).count()
        if (i != 0):
            messages.error(newrequest, u"Email Address already registered, please login.", 'email')
            bFlashMessage = True  

        # Password - Required; No fewer than 8 characters in length; matches Password Confirmation
        # Password should be more than 8 characters
        if len(pwd) < 8:
            messages.error(newrequest,u"Password must be at least 8 characters in length.", extra_tags='pwd')
            bFlashMessage = True

        # Password and Password Confirmation should match
        if pwd != confpwd:
            messages.error(newrequest,"Password fields do not match!", extra_tags='pwd')
            bFlashMessage = True

        return bFlashMessage

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)    
    email = models.CharField(max_length=255)    
    pwhashval = models.CharField(max_length=255)    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"