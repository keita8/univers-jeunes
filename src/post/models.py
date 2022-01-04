from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse, reverse_lazy
from tinymce.models import HTMLField
from tinymce import models as tinymce_models
from ckeditor.fields import RichTextField


User = get_user_model()



class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Nom de l\'editeur')
    profile_pic = models.ImageField(verbose_name='photo')

    class Meta:
        verbose_name = 'Editeur'
        verbose_name_plural = 'Editeurs'

    def __str__(self):
        return f' {self.user.username} '
# Create your models here.
# ---------------------------CATEGORIES--------------------------
# MODELE LIE AUX CATEGORIES
class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name="Categorie")

    class Meta:
        verbose_name = 'Categorie'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.title}'



#-------------------------ARTICLES-------------------------------
# MODELE LIE AUX ARTICLES
class Post(models.Model):
    title         = models.CharField(max_length=200, verbose_name='Titre')
    overview      = HTMLField('Aperçu', default=' ')
    content       = HTMLField('Contenu', default=' ')
    timestamp     = models.DateTimeField(auto_now_add=True, verbose_name='Date de publication')
    comment_count = models.IntegerField(default=0, verbose_name='Compteur de commentaire')
    view_count    = models.IntegerField(default=0, verbose_name='Nombre de vue')
    author        = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Editeur')
    thumbnail     = models.ImageField(verbose_name="Photo de l'article")
    categories    = models.ManyToManyField(Category)
    featured      = models.BooleanField(default=False, verbose_name='Publié ?')
    previous_post = models.ForeignKey('self', related_name='previous', on_delete=models.SET_NULL, verbose_name='Article precendent', blank=True, null=True)
    next_post     = models.ForeignKey('self', related_name='next', on_delete=models.SET_NULL, verbose_name='Article suivant', blank=True, null=True)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return f'{self.title}'


    def get_absolute_url(self):
        return reverse('post', kwargs={'id':self.id})

    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')




class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Editeur ayant commenté')
    timestamp = models.DateTimeField(auto_now_add=True ,verbose_name='Date du commentaire')
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE, verbose_name='Article commenté')
    content = models.TextField(verbose_name='Commentaire')

    class Meta:
        verbose_name = 'Commentaire'
        verbose_name_plural = 'Commentaires'

    def __str__(self):
        return f'{self.user}'
