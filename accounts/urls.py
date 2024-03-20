from django.conf.urls import path
from .views import *

app_name = "accounts"

urlpatterns = [

    path(r'^login/$', login_view, name='login'),
    path(r'^logout/$', logout_view, name='logout'),
]
