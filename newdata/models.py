from django.db import models
from django.contrib.auth.models import User
from accounts.models import Player

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
    training_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    total_distance = models.IntegerField(null=False, blank=False)
    high_speed_distance = models.IntegerField(null=False, blank=False)
    sprint_distance = models.IntegerField(null=False, blank=False)
    hmld = models.IntegerField(null=False, blank=False)
    total_acc_deacc = models.IntegerField(null=False, blank=False)
    max_speed = models.DecimalField(max_digits=4, decimal_places=2, null=False, blank=False)

    def __str__(self):
        return f"User: {self.player.name}"