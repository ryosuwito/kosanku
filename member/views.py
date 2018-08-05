# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse
from .forms import UserForm, MemberForm, LoginForm

def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, prefix="user_form")
        member_form = MemberForm(request.POST, request.FILES, prefix="member_form")
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data.get('password'))
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        if member_form.is_valid():
            member = member_form.save()
            member.user = user
        return HttpResponse("%s, %s"%(user.member.nama_lengkap, user.member.profile_photo))
    else:
        user_form = UserForm(prefix="user_form")
        member_form = MemberForm(prefix="member_form")   
    return render(request, "member/daftar.html", {"user_form":user_form, "mode":"pemilik", "member_form":member_form})

def daftar(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, prefix="user_form")
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data.get('password'))
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return HttpResponse("Success")
    else:
        user_form = UserForm(prefix="user_form")
    return render(request, "member/daftar.html", {"user_form":user_form, "mode":"pencari"})

def login_member(request):
    if request.method == 'POST':
        user_form = LoginForm(request.POST)
        if user_form.is_valid():
            username = user_form.cleaned_data.get('username')
            password = user_form.cleaned_data.get('password')
            user = authenticate(request,username=username, password=password)
            login(request, user)
            return HttpResponse("Success")
    else:
        user_form = LoginForm()
    return render(request, "member/login.html", {"user_form":user_form, "mode":"pencari"})

def pre_register(request):
    return render(request, "member/pre_register.html")

@login_required(login_url="/login/")
def profile(request):
    return render(request, "member/profile.html")

@login_required(login_url="/login/")
def logout_member(request):
    logout(request)
    return redirect(reverse("login"))
