# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import messages
from apps.login_registration.models import User

class QuoteManager(models.Manager):
    def basic_validator(self, newrequest):
        bFlashMessage = False

        author = newrequest.POST['author']
        text = newrequest.POST['text']


        # Author Name - Required; Can't be blank
        if len(author) < 1:
            messages.error(newrequest, u"Author Name cannot be blank", extra_tags="author")
            bFlashMessage = True  

        # Quote Text - Required; Can't be blank
        if len(text) < 1:
            messages.error(newrequest, u"Quote text cannot be blank", extra_tags="text")
            bFlashMessage = True  

        return bFlashMessage

class Quote(models.Model):
    author = models.CharField(max_length=255)
    text = models.TextField(max_length=1000, blank=True, null=True)    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # Now we handle the relationsips
    posted_by = models.ForeignKey(User, related_name="quotes_posted")
    users_who_like = models.ManyToManyField(User, related_name="liked_quotes")
    objects = QuoteManager()
