# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import re, bcrypt

from .models import *

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX  = re.compile('[0-9]')

# the index function is called when root is visited

def index(request):
    print("index()")

    if "user_id" not in request.session:
        return redirect("/login_registration")

    all_qoutes = Quote.objects.all()
    print(all_qoutes)
    
    context = {
        "user": User.objects.get(id=request.session['user_id']),
        "all_qoutes": all_qoutes,
    }
    
    return render(request, "dashboard.html", context)

def process_add(request):
    print("process_add()")

    if request.method == "POST":
        bFlashMessage = Quote.objects.basic_validator(request)

    if bFlashMessage == True:
        request.session["add_attempt_failed"] = "YES"
        request.session['author'] = request.POST['author']
        request.session['text'] = request.POST['text']
        return redirect('/')

    add_author = request.POST['author']
    add_text = request.POST['text']
    add_user_id = request.session['user_id']

    print(add_author)
    print(add_text)
    print(add_user_id)
        
    objQuote = Quote.objects.create(author=add_author, text=add_text, posted_by_id=int(add_user_id))

    return redirect('/quotes')

def process_delete(request):
    print("process_delete()")

    if request.method == "POST":
        post_to_delete = request.POST['post_id']
        objQuote = Quote.objects.get(id=int(post_to_delete))
        objQuote.delete()

    return redirect('/quotes')

def show_user(request, userid):

    if "user_id" not in request.session:
        return redirect("/login_registration")

    user = User.objects.get(id=int(userid))
    posted_quotes = User.objects.get(id=int(userid)).quotes_posted.all().values()    

    context = {
        "posted_quotes": posted_quotes,
        "user": user,
    }

    return render(request, "showuser.html", context)

def edit_user(request, userid):

    if "user_id" not in request.session:
        return redirect("/login_registration")

    user = User.objects.get(id=int(userid))

    context = {
        "user": user,
    }

    return render(request, "edituser.html", context)

def process_edit(request):
    print("process_edit()")

    if request.method == "POST":
        bFlashMessage = User.objects.basic_validator(request)

        request.session["first_name"] = request.POST['first_name']
        request.session["last_name"] = request.POST['last_name']
        request.session["email"] = request.POST['email']

        f_name = request.POST['first_name']
        l_name = request.POST['last_name']
        email = request.POST['email']
        uid = request.POST['userid']

    if bFlashMessage:
        request.session["edit_attempt_failed"] = True
        return redirect("/myaccount/" + uid)
    else:
        request.session.clear()
        user_to_edit = User.objects.get(id=int(uid))
        user_to_edit.first_name = f_name
        user_to_edit.last_name = l_name
        user_to_edit.email = email
        user.save()

    return redirect('/quotes')

def process_like(request):
    print("process_like()")

    if request.method == "POST":


        quote_id = request.POST['quote_id']
        user_id = request.POST['user_id']

        User.objects.get(id=int(user_id)).liked_quotes.add(Quote.objects.get(id=int(quote_id)))     

    return redirect('/quotes')    


def logoff(request):
    print("logoff()")
    request.session.clear()
    return redirect('/')   