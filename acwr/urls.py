from django.urls import path, include
from home.views import home_view
from django.contrib import admin
from accounts.views import login_view, logout_view
from matchday.views import matchday_view
from newdata.views import NewDataView, get_training_list, add_training, add_training_submit, add_training_cancel
from newdata.views import delete_training

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'login/', login_view, name='login'),
    path(r'logout/', logout_view, name='logout'),
    path(r'maxmatchday/', matchday_view, name='matchday'),
    path(r'newdata/get_student_list', get_training_list, name='get_training_list'),
    path(r'newdata/add_student', add_training, name='add_training'),
    path(r'newdata/add_student_submit', add_training_submit, name='add_training_submit'),
    path(r'newdata/add_student_cancel', add_training_cancel, name='add_training_cancel'),
    path(r'newdata/<int:training_pk>/delete_student', delete_training, name='delete_training'),
    path(r'newdata/', NewDataView.as_view(), name='newdata'),
    path('', home_view, name='home')
]