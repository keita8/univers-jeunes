from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.


class Post(model.Model):
    title = models.CharField(max_length=200, verbose_name='Titre')
    overview = models.CharField(max_length=200, verbose_name='Apercu')
