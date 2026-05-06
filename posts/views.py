import django_filters
from django.db.models import QuerySet
from django.views import generic
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, generics, mixins
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from posts.models import Post
from posts.serializers import PostSerializer
from .permissions import AuthorOrReadOnly





from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, generics, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.decorators import api_view, permission_classes
from posts.models import Post
from posts.serializers import PostSerializer
from .permissions import AuthorOrReadOnly

@api_view(http_method_names=['GET', 'POST'])
@permission_classes([AllowAny])
def homepage(request: Request):
    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)  # ✅ removed many=True
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Post created successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'message': 'Hello World!'})


class PostListCreateView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['title', 'created']
    search_fields = ['title', 'content']



    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostRetrieveUpdateDeleteView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [AuthorOrReadOnly]

    def get(self, request: Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request: Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request: Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)




