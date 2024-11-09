from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TareaViewSet

router = DefaultRouter()
router.register(r'tasks', TareaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
