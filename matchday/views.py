from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from django import forms
from accounts.models import MaxMatchData
from django.contrib import messages

class MaxMatchDay(TemplateView):
    template_name = 'matchday.html'

class MaxMatchDayDataForm(forms.ModelForm):
    player = forms.ModelChoiceField(queryset=None, label="Select Player")

    class Meta:
        model = MaxMatchData
        fields = ('player', 'duration', 'total_distance', 'high_speed_distance', 'sprint_distance', 'hmld', 'total_acc_deacc', 'max_speed')

    def __init__(self, *args, **kwargs):
        team_players = kwargs.pop('team_players', None)
        super(MaxMatchDayDataForm, self).__init__(*args, **kwargs)
        if team_players:
            self.fields['player'].queryset = team_players


def get_matchday(request):
    context = {}
    profile = request.user.profile
    team = profile.team
    matchdaydata = MaxMatchData.objects.filter(player__team=team)
    context = {'matchdaydatas': matchdaydata}
    return render(request, 'matchday_list.html', context)


def add_matchday(request):
    team_players = request.user.profile.team.team_players.all()
    if not team_players:
        messages.error(request, 'There is no player added for this account, please firstly add players !')
    form = MaxMatchDayDataForm(team_players=team_players)
    context = {'form': form}
    return render(request, 'add_matchday.html', context)


def add_matchday_submit(request):
    context = {}
    team_players = request.user.profile.team.team_players.all()
    form = MaxMatchDayDataForm(request.POST, request.FILES, team_players=team_players)
    context['form'] = form
    if form.is_valid():
        old_matchday_data = form.cleaned_data.get('player')
        existing_data = MaxMatchData.objects.filter(player=old_matchday_data)
        if existing_data.exists():
            existing_data.delete()
            context['matchdaydata'] = form.save()
            return HttpResponse('<script>location.reload(true);</script>')
        context['matchdaydata'] = form.save()
        return render(request, 'matchday_row.html', context)
    else:
        return render(request, 'add_matchday.html', context)



def add_matchday_cancel(request):
    return HttpResponse()

def delete_matchday(request, matchday_pk):
    matchdaydata = MaxMatchData.objects.get(pk=matchday_pk)
    matchdaydata.delete()
    return HttpResponse()
