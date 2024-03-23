import uuid
import datetime
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    ADMIN = 1
    USER = 2
    TESTUSER = 3
    ROLE_CHOICES = (
        (ADMIN, 'ADMIN'),
        (USER, 'USER'),
        (TESTUSER, 'TESTUSER'),
    )
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True, default=USER)
    team = models.ForeignKey('Team', related_name='player', on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return str(self.user)

class Team(models.Model):
    name = models.CharField(max_length=100, verbose_name="Team Name")
    # Diğer gerekli alanlar eklenebilir
    def __str__(self):
        return str(self.name)

class Player(models.Model):
    MALE = 1
    FEMALE = 2
    OTHER = 3
    GENDER_CHOICES = (
        (MALE, 'MALE'),
        (FEMALE, 'FEMALE'),
        (OTHER, 'OTHER'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    team = models.ForeignKey(Team, related_name='team_players', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, blank=False)
    height = models.IntegerField(null=True, blank=True, default=180)
    weight = models.IntegerField(null=True, blank=True, default=72)
    birthday = models.DateField(null=True, blank=True, default=datetime.date.today)
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, default=1, null=True, blank=True)
    def __str__(self):
        return str(self.name)

class MaxMatchData(models.Model):
    player = models.ForeignKey(Player, related_name='max_match_values', on_delete=models.CASCADE)
    duration = models.IntegerField(null=False, blank=False, default=90)
    total_distance = models.IntegerField(null=False, blank=False, default=10000)
    high_speed_distance = models.IntegerField(null=False, blank=False, default=600)
    sprint_distance = models.IntegerField(null=False, blank=False, default=300)
    hmld = models.IntegerField(null=False, blank=False, default=500)
    total_acc_deacc = models.IntegerField(null=False, blank=False, default=120)
    max_speed = models.DecimalField(max_digits=4, decimal_places=2, null=False, blank=False, default=25.12)

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)