from django import forms
from .models import TrainingData

class TrainingDataForm(forms.ModelForm):
    class Meta:
        model = TrainingData
        fields = ['player', 'training_type', 'training_date', 'start_time', 'end_time', 'total_distance', 'high_speed_distance', 'hmld', 'total_acc_deacc', 'max_speed']
