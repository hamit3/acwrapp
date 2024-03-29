from django.urls import path, include
from home.views import home_view
from django.contrib import admin
from accounts.views import login_view, logout_view,signup_view
from matchday.views import MaxMatchDay, add_matchday, add_matchday_submit,add_matchday_cancel,delete_matchday,get_matchday
from newdata.views import NewDataView, get_training_list, add_training, add_training_submit, add_training_cancel
from newdata.views import delete_training
from player.views import PlayerView, get_player_list, add_player, add_player_submit, add_player_cancel, delete_player


urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'login/', login_view, name='login'),
    path(r'logout/', logout_view, name='logout'),
    path(r'signup/', signup_view, name='signup'),

    path(r'maxmatchday/get_matchday_list', get_matchday, name='get_matchday'),
    path(r'maxmatchday/add_matchday', add_matchday, name='add_matchday'),
    path(r'maxmatchday/add_matchday_submit', add_matchday_submit, name='add_matchday_submit'),
    path(r'maxmatchday/add_matchday_cancel', add_matchday_cancel, name='add_matchday_cancel'),
    path(r'maxmatchday/<int:matchday_pk>/delete_matchday', delete_matchday, name='delete_matchday'),
    path(r'maxmatchday/', MaxMatchDay.as_view(), name='matchday'),

    path(r'newdata/get_training_list', get_training_list, name='get_training_list'),
    path(r'newdata/add_training', add_training, name='add_training'),
    path(r'newdata/add_training_submit', add_training_submit, name='add_training_submit'),
    path(r'newdata/add_training_cancel', add_training_cancel, name='add_training_cancel'),
    path(r'newdata/<int:training_pk>/delete_training', delete_training, name='delete_training'),
    path(r'newdata/', NewDataView.as_view(), name='newdata'),

    path(r'player/get_player_list', get_player_list, name='get_player_list'),
    path(r'player/add_player', add_player, name='add_player'),
    path(r'player/add_player_submit', add_player_submit, name='add_player_submit'),
    path(r'player/add_player_cancel', add_player_cancel, name='add_player_cancel'),
    path(r'player/<uuid:player_pk>/delete_player', delete_player, name='delete_player'),
    path(r'player/', PlayerView.as_view(), name='player'),

    path('', home_view, name='home')
]