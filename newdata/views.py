import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from newdata.models import TrainingData
from django.views.generic import TemplateView
from django import forms


class NewDataView(TemplateView):
    template_name = 'newdata.html'

class TrainingDataForm(forms.ModelForm):
    class Meta:
        model = TrainingData
        exclude = []

def get_training_list(request):
    context = {}
    profile = request.user.profile
    team = profile.team
    training_data = TrainingData.objects.filter(player__team=team).order_by('-id')
    context['training_datas'] = training_data
    return render(request, 'training_list.html', context)


def add_training(request):
    context = {'form': TrainingDataForm()}
    return render(request, 'add_training.html', context)


def add_training_submit(request):
    context = {}
    form = TrainingDataForm(request.POST, request.FILES)
    context['form'] = form
    if form.is_valid():
        context['training_data'] = form.save()
    else:
        return render(request, 'add_training.html', context)
    return render(request, 'training_row.html', context)


def add_training_cancel(request):
    return HttpResponse()

def delete_training(request, training_pk):
    training_data = TrainingData.objects.get(pk=training_pk)
    training_data.delete()
    return HttpResponse()
