from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .models import Blog, Comment
from .serializers import BlogSerial  # Updated name
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken  # For JWT Token

class BlogPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
    ordering = '-created_at'  # Corrected typo

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerial  # Updated name
    pagination_class = BlogPagination
    permission_classes = [IsAuthenticated]

# Register a New User
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Authenticate a User
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password']
            )
            if user:
                # Generate JWT token
                refresh = RefreshToken.for_user(user)
                return Response({
                    "message": "Login successful!",
                    "access_token": str(refresh.access_token),  # Return the access token
                }, status=status.HTTP_200_OK)
            return Response({"message": "Invalid credentials!"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Manage Users (Retrieve, Update, Delete)
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
