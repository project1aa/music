from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('music.urls', namespace='music')),
    path('news', include('news.urls', namespace='news')),
    path('contact_us', include('contact_us.urls', namespace='contact_us')),
    path('short', include('shorturls.urls')),
    path('maintenance-mode', include('maintenance_mode.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
