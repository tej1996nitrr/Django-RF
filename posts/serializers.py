from rest_framework import serializers
from .models import Post,Category
from django.contrib.auth import get_user_model

class CategorySerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Category
            fields= ('url', 'name')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('category', 'id','author','title','content','created_at',)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id' ,'username')
