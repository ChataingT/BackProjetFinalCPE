from django.urls import path, include
from rest_framework import routers
from . import views
from notification.urls import router as notificationRouter

router = routers.DefaultRouter()
router.registry.extend(notificationRouter.registry)
router.register(r'challenge', views.ChallengeViewSet, basename='challenge')

urlpatterns = [
        path(r'', include(router.urls)),
        ]
