from django.shortcuts import render

# Create your views here.
from rest_framework import response, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from blog.models import Category, Post
from blog.serializers import CategorySerializer, PostSerializer


@api_view(['GET'])
def hello_world(request):
    return Response('Hello, World!')


@api_view(['GET'])
def sechan(request):
    return Response('sechan')


@api_view(['GET'])
def get_categories(request):
    queryset = Category.objects.all()
    serialized = CategorySerializer(queryset, many=True)
    return Response(serialized.data)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
