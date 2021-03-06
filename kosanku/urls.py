"""kosanku URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from member.views import register, daftar, login_member, pre_register, profile, logout_member
from kost.views import index, add_kost, detail_kost
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', index, name="home"),
    url(r'^admin/', admin.site.urls),
    url(r'^add/$', add_kost, name="add_kost"),
    url(r'^detail/$', detail_kost, name="detail_kost"),
    url(r'^login/$', login_member, name="login"),
    url(r'^logout/$', logout_member, name="logout"),
    url(r'^pre/$', pre_register, name="pre_register"),
    url(r'^daftar/$', daftar, name="daftar_pencari"),
    url(r'^profile/$', profile, name="profile"),
    url(r'^register/$', register, name="daftar_pemilik")
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)