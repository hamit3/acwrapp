from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from django import forms
from accounts.models import MaxMatchData

class MaxMatchDay(TemplateView):
    template_name = 'matchday.html'

class MaxMatchDayDataForm(forms.ModelForm):
    class Meta:
        model = MaxMatchData
        exclude = []

def get_matchday(request):
    context = {}
    team = request.user.profile.team.name
    matchdaydata = MaxMatchData.objects.all()
    context = {'matchdaydatas': matchdaydata}
    return render(request, 'matchday_list.html', context)


def add_matchday(request):
    context = {'form': MaxMatchDayDataForm()}
    return render(request, 'add_matchday.html', context)

def add_matchday_submit(request):
    context = {}
    form = MaxMatchDayDataForm(request.POST, request.FILES)
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
