# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    profile_photo = models.ImageField(upload_to = "profile_photo/%Y/%m/%d/", blank=True)
    nama_lengkap = models.CharField(max_length=255, blank=True)
    alamat_lengkap = models.CharField(max_length=400, blank=True)
    is_pemilik_kost = models.BooleanField(default=False, blank=True)

