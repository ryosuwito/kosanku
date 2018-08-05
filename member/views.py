# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import login, authenticate
from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm, MemberForm

def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, prefix="user_form")
        member_form = MemberForm(request.POST, request.FILES, prefix="member_form")
        if user_form.is_valid:
            user = user_form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        if member_form.is_valid:
            member = member_form.save()
            member.user = user
        return HttpResponse("%s, %s"%(user.member.nama_lengkap, user.member.profile_photo))
    else:
        user_form = UserForm(prefix="user_form")
        member_form = MemberForm(prefix="member_form")   
    return render(request, "member/daftar.html", {"user_form":user_form, "member_form":member_form})
