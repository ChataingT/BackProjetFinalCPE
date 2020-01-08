from django.urls import path, include
from rest_framework import routers
from . import views
from users.urls import router as userRouter

router = routers.DefaultRouter()
router.registry.extend(userRouter.registry)
router.register(r'activity', views.ActivityViewSet, basename='activity')

urlpatterns = [
#        path(r'', include(router.urls)), do not uncomment, done in planning/urls.py
        ]
