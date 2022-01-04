from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

from post.views import (
  home, 
  blog, 
  post,
  search


  )



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('blog/', blog, name='blog'),
    path('search/', search, name='search'),
    path('post/<int:id>/', post, name='post'),
    path('marketing/', include('marketing.urls')),
    path('tinymce/', include('tinymce.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
