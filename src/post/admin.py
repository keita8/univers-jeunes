from django.contrib import admin
from .models import Author, Category, Post, Comment
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'author', 'timestamp']
    list_display_links = ['id','title', 'author']
    
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
