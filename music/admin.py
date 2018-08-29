from django.contrib import admin
from .models import Song, Singer, Genre


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    # readonly field
    readonly_fields = ('duration', 'views',)
    # search fields
    search_fields = ('name', 'singer__name')

    # fields
    fields = ('name', 'singer', 'genres',
        'file1', 'file2', 'image', 'lyrics', 'tags', 'duration', 'views')

    # display fields for index
    def singer_name(self, obj):
        return obj

    def singer(self, obj):
        return obj.name

    def get_genres(self, obj):
        return obj.list_genres()
    get_genres.short_description = 'genres'

    list_display = ('name', 'singer', 'get_genres', 'duration')

    # automatically slugify song name
    # prepopulated_fields = {'slug': ('name',)}

    def get_readonly_fields(self, request, obj=None):
        if obj:
            self.prepopulated_fields = {}
            return self.readonly_fields + ('slug',)
        return self.readonly_fields

#admin.site.register(Song)
admin.site.register(Singer)
admin.site.register(Genre)
