from django.shortcuts import render
from .models import Post,Category
from .serializers import PostSerializer, CategorySerializer,UserSerializer
from rest_framework import viewsets, permissions
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model

class PostView(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class CategoryView(viewsets.ModelViewSet):
    queryset  =Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer