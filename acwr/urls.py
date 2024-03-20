from django.urls import path
from home.views import home_view
from django.contrib import admin
from accounts.views import login_view, logout_view
from matchday.views import matchday_view
from newdata.views import newdata_view

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'login/', login_view, name='login'),
    path(r'logout/', logout_view, name='logout'),
    path(r'maxmatchday/', matchday_view, name='matchday'),
    path(r'newdata/', newdata_view, name='newdata'),
    path('', home_view, name='home'),
]