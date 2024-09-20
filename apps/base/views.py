from rest_framework import viewsets
from apps.base.models import LandingSection, Post
from apps.base.serializers import LandingSectionSerializer, PostSerializer

class LandingSectionViewSet(viewsets.ModelViewSet):
    queryset = LandingSection.objects.all()
    serializer_class = LandingSectionSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
