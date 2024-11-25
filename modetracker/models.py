from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class DailyFeeling(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    feeling = models.CharField(max_length=20, choices=[
        ('Angry', 'Angry'),
        ('Sad', 'Sad'),
        ('Ok', 'Ok'),
        ('Good', 'Good'),
        ('Happy', 'Happy')

    ])

    def __str__(self):
        return f'{self.user.username} - {self.date} - {self.feeling}'