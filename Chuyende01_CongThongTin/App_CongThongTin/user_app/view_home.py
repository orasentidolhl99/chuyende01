from django.contrib.auth import logout,login,authenticate,update_session_auth_hash
from django.shortcuts import render,redirect
from django.contrib import messages
from ..forms import *

def home(request):
    return render(request,'base_home_user.html')

def lienhe(request):
    return render(request, 'Menu_trang/header_lienhe.html')

