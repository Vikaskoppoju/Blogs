from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogViewSet,UserViewSet,RegisterView, LoginView,CommentViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
# Create a router and register the BlogViewSet
router = DefaultRouter()
router.register(r'blogs', BlogViewSet)
router.register(r'users', UserViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


