from django.urls import path
from . import views


app_name = 'music'

urlpatterns = [
    path('', views.SongListView.as_view(), name='index'),
    path('<int:pk>', views.SongDetailView.as_view(), name='detail'),
]
