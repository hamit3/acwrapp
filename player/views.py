from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django import forms
from accounts.models import Player

class PlayerView(TemplateView):
    template_name = 'players.html'

class PlayerDataForm(forms.ModelForm):
    class Meta:
        model = Player
        exclude = []

def get_player_list(request):
    context = {}
    profile = request.user.profile
    team = profile.team
    players = Player.objects.all().filter(team=team)
    context['players'] = players
    return render(request, 'player_list.html', context)


def add_player(request):
    context = {'form': PlayerDataForm()}
    return render(request, 'add_player.html', context)


def add_player_submit(request):
    context = {}
    form = PlayerDataForm(request.POST, request.FILES)
    context['form'] = form
    print(context)
    if form.is_valid():
        context['player'] = form.save()
    else:
        return render(request, 'add_player.html', context)
    return render(request, 'player_row.html', context)


def add_player_cancel(request):
    return HttpResponse()

def delete_player(request, player_pk):
    player = Player.objects.get(pk=player_pk)
    player.delete()
    return HttpResponse()
