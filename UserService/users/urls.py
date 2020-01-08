# users/urls.py
from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'users', views.CustomUserViewSet, basename='users')


urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
#    path('', include(router.urls)), DO not uncomment if this line is present in an other app 
]