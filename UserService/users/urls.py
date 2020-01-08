# users/urls.py
from django.urls import path, include
from rest_framework import routers
from .views import SignUpView
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.CustomUserViewSet, basename='users')


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]