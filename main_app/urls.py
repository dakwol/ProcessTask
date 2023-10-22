from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LifeSituationViewSet

router = DefaultRouter()
router.register(r'lifesituations', LifeSituationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
