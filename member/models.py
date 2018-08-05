# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to = 'profile_photo', blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        member = Member(user=instance)
        member.referal_code = Member.get_referal();
        member.qrcode = Member.get_qrcode(name=member.referal_code,
            content=instance.username);
        member.save()
        
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.member.save()

