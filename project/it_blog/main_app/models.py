from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=64, unique=True)
    subtitle = models.CharField(max_length=128, blank=True)
    post_datetime = models.DateTimeField(auto_now=True)
    text = models.TextField()
    is_active = models.BooleanField(default=False)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.title