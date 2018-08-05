# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    return render(request,"kost/home.html")

def add_kost(request):
    return render(request,"kost/add_product.html")

def detail_kost(request):
    return render(request, "kost/product_detail.html")