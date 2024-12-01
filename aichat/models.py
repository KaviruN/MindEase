from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.username)

class ChatData(models.Model):
    user_chat = models.ForeignKey(UserData, related_name='user_data',on_delete=models.CASCADE)
    prompt = models.CharField(max_length=125)
    response = models.TextField(max_length=10000)
    created = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.created)
    
    class Meta:
        ordering = ['-created']