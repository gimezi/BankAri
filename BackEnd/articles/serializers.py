from rest_framework import serializers
from .models import Article, Comment
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('nickname', 'id')
        read_only_fields = ['nickname', 'id']


class ArticleListSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'user', 'created_at')


class ArticleSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Article
        fields = '__all__'
        # read_only_fields = ('user',)

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    Article_set = ArticleSerializer(many=True, read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)


class ArticleCommentSerializer(serializers.Serializer):
    article = ArticleSerializer()
    comments = CommentSerializer(many=True)
