from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import LandingSectionViewSet, PostViewSet

# Создаем роутер
router = DefaultRouter()
router.register(r'sections', LandingSectionViewSet, basename='landing-sections')
router.register(r'posts', PostViewSet, basename='posts')

urlpatterns = [
    path('', include(router.urls)),  # Все маршруты из роутера
]
