from django.contrib import admin
from .models import Song, Singer, Genre


admin.site.register(Song)
admin.site.register(Singer)
admin.site.register(Genre)
