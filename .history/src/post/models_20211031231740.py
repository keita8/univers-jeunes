from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Author(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Nom de l\'editeur')
    user_photo = models.ImageField(
        upload_to='media_root', verbose_name='photo')
# Create your models here.
# ---------------------------ARTICLES--------------------------
# MODELE LIE AUX ARTICLES


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titre')
    overview = models.TextField(max_length=200, verbose_name='Apercu')
    timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name='Date de publication')
    comment_count = models.InterField(
        default=0, verbose_name='Compteur de commentaire')
    author = models.ForeignKey(
        User, on_delete=model.CASCADE, verbose_name='Editeur')

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return f'{self.title} {self.timestamp}'
