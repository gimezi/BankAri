from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.core.serializers import serialize
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer, ArticleCommentSerializer
from .models import Article, Comment



@api_view(['GET', 'POST'])
def article_list(request):
    # 전체 글 조회
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    # 새로운 글 작성
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # serializer.save()
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comments = article.comment_set.all()

    # 특정 글 + 해당 글에 달린 댓글 조회
    if request.method == 'GET':
        combination = {
            'article' : article,
            'comments' : comments
        }
        serializer = ArticleCommentSerializer(combination)
        return Response(serializer.data)
    
    # 특정 글에서 댓글 작성
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article, user=request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
    # 글 삭제
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    # 글 수정
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 댓글 삭제x
@api_view(['DELETE'])
def comment_delete(request, article_pk, comment_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment = article.comment_set.get(pk=comment_pk)
    if request.method == 'DELETE':
        comment.delete()
        comments =article.comment_set.all()
        combination = {
            'article' : article,
            'comments': comments
        }
        serializer = ArticleCommentSerializer(combination)
        return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)
    
