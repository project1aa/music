from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Song


class SongListView(ListView):
    model = Song

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        latest_songs = Song.objects.all()[:10]
        context['latest_songs'] = latest_songs
        return context


class SongDetailView(DetailView):
    model = Song
