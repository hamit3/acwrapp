from django.db import models
from django.contrib.auth.models import User
from accounts.models import Player
import datetime

class TrainingData(models.Model):
    TRAINING = 1
    MATCH = 2
    REGENERATION = 3
    REHABILITATION = 4
    OTHER = 5
    TRAINING_TYPE_CHOICES = (
        (TRAINING, 'TRAINING'),
        (MATCH, 'MATCH'),
        (REGENERATION, 'REGENERATION'),
        (REHABILITATION, 'REHABILITATION'),
        (OTHER, 'OTHER'),
    )
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='training_data')
    training_type = models.PositiveSmallIntegerField(choices=TRAINING_TYPE_CHOICES, default=1, null=False, blank=False)
    training_date = models.DateField(null=True, blank=True, default=datetime.date.today)
    duration = models.IntegerField(null=True, blank=True, default='90')
    total_distance = models.IntegerField(null=True, blank=True, default='10000')
    high_speed_distance = models.IntegerField(null=True, blank=True, default='300')
    sprint_distance = models.IntegerField(null=True, blank=True, default='200')
    hmld = models.IntegerField(null=True, blank=True, default='700')
    total_acc_deacc = models.IntegerField(null=True, blank=True, default='0')
    max_speed = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, default=0)

    def __str__(self):
        return f"User: {self.player.name}"