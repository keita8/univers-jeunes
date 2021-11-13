from django.contrib import admin
from .models import Dernieretendance
# Register your models here.

class tendanceAdmin(admin.ModelAdmin):
	list_display_links = ['title']
	list_display = ['title', ]
	list_filter = ['title', 'content']


admin.site.register(Dernieretendance, tendanceAdmin)