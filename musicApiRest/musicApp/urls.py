from django.urls import path
from .views import MusicListCreateView, MusicRetrieveUpdateDestroyView

urlpatterns = [
    path('musics/', MusicListCreateView.as_view(), name='music-list-create'),
    path('musics/<int:pk>/', MusicRetrieveUpdateDestroyView.as_view(), name='music-detail'),
]