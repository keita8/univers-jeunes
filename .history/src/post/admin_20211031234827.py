from django.contrib import admin
from .models import Author, Category, Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp']
    
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
