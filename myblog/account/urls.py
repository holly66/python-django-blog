from django.conf.urls import url
from . import views

from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/$', auth_views.login, name='user_login'),
    url(r'^logout/$', auth_views.logout,name='user_logout'),
]