from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LifeSituationViewSet, ServiceViewSet, ProcessViewSet

router = DefaultRouter()
router.register(r'lifesituations', LifeSituationViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'processes', ProcessViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
