from gc import get_objects

import rest_framework
from django.db.models import QuerySet
from django.shortcuts import get_object_or_404
from rest_framework import viewsets,status
from rest_framework.request import Request
from rest_framework.response import Response
from posts.serializers import PostSerializer
from .models import Post


class PostViewSet(viewsets.ModelViewSet ):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

















