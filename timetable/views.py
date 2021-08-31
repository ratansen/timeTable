from django.shortcuts import render
from django.contrib.messages.api import error
from django.http import HttpResponseRedirect, response
from django.db.models import query
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def index(request):
    return render(request,'index.html')

