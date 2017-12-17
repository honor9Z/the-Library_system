"""weekwork1 URL Configuration

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
from app01 import views
from app01.views import pcgetcaptcha

from app01.views import pcajax_validate

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index),
    url(r'^$', views.index),
    url(r'^book/', views.book),
    url(r'^addbook/', views.addbook),
    url(r'^edit/', views.edit),
    url(r'^delbook/(\d+)', views.delbook),
    url(r'^author/', views.author),
    url(r'^editauthor/', views.editauthor),
    url(r'^delauthor/(\d+)', views.delauthor),
    url(r'^addauthor/', views.addauthor),
    url(r'^publish/', views.publish),
    url(r'^addpublish/', views.addpublish),
    url(r'^editpublish/', views.editpublish),
    url(r'^delpublish/(\d+)', views.delpublish),
    url(r'^reg/', views.reg),
    url(r'^login/', views.log_in),
    url(r'^logout/', views.log_out),
    url(r'^set_pwd/', views.set_pwd),

    #验证码
    url(r'^pc-geetest/register', pcgetcaptcha, name='pcgetcaptcha'),

    url(r'^pc-geetest/ajax_validate',pcajax_validate, name='pcajax_validate'),




]
