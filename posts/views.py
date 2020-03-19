from django.shortcuts import render
from .models import Post,Category
from .serializers import PostSerializer, CategorySerializer
from rest_framework import viewsets

class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    

class CategoryView(viewsets.ModelViewSet):
    queryset  =Category.objects.all()
    serializer_class = CategorySerializer