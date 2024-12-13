from rest_framework import generics
from .models import Music
from .serializers import MusicSerializer

class MusicListCreateView(generics.ListCreateAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

class MusicRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer