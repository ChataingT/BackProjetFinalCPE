from django.urls import path, include
from rest_framework import routers
from . import views
from activity.urls import router as activityRouter

router = routers.DefaultRouter()
router.registry.extend(activityRouter.registry)
router.register(r'notification', views.NotificationViewSet, basename='notification')

urlpatterns = [
    #    path(r'', include(router.urls)), do not uncomment, done in challenge/urls.py
        ]
