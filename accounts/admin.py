from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Profile, Team, Player, MaxMatchData

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'role', 'team']

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Player)
class PlayersAdmin(admin.ModelAdmin):
    list_display = ['id', 'team', 'name', 'height', 'weight', 'birthday', 'gender',]


@admin.register(MaxMatchData)
class MaxMatchData(admin.ModelAdmin):
    list_display = ['player', 'duration', 'total_distance', 'high_speed_distance', 'sprint_distance', 'hmld', 'total_acc_deacc', 'max_speed']

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)