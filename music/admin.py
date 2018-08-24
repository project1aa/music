from django.contrib import admin
from .models import Song, Singer, Genre


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    # readonly field
    readonly_fields = ('duration', 'views',)
    # search fields
    search_fields = ('name', 'singer__name')
    # display fields for index
    def singer_name(self, obj):
        return obj

    def singer(self, obj):
        return obj.name

    def get_genres(self, obj):
        return obj.list_genres()
    get_genres.short_description = 'genres'

    list_display = ('name', 'singer', 'get_genres', 'duration')


#admin.site.register(Song)
admin.site.register(Singer)
admin.site.register(Genre)
