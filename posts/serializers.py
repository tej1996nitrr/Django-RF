from rest_framework import serializers
from .models import Post,Category

class CategorySerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Category
            fields= ('url', 'name')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('category', 'id','author','title','content','created_at',)