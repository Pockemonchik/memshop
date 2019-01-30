from django.db import models
from django.contrib.auth.models import User
from django.conf.urls import url
from django.urls import reverse

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile',on_delete="cascade",primary_key=True)
    user_picture = models.ImageField(upload_to='media', blank=True, null=True)
    user_balance = models.IntegerField(default=0)
    def get_absolute_url(self):
        return reverse('detail_profile', args=[str(self.id)])
    def __str__(self):
        return self.user.username
