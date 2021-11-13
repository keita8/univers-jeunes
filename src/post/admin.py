from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Post, Category, Author, Comment, PostView, Banner
# Register your models here.

class PostAdmin(admin.ModelAdmin):
	list_display = [ 'id' ,'title', 'status', 'author']
	prepopulated_fields = {'slug': ('title', )}
	list_filter = ('author', )
	list_display_links = [ 'id' ,'title']
	ordering = ('-timestamp', )


# class CommentAdmin(admin.ModelAdmin):
# 	list_display = ['timestamp']


class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Author)
admin.site.register(PostView)
admin.site.register(Banner)
admin.site.register(Comment)

# admin.site.unregister(Group)
admin.site.site_header = 'Blog'
admin.site.site_title = 'Blog'
