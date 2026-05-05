from django.db.models import QuerySet
from rest_framework.request import Request
from rest_framework.response import  Response
from rest_framework import status, generics,mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,APIView
from posts.models import Post
from posts.serializers import PostSerializer
from django.shortcuts import get_object_or_404


# 📌 Dummy posts data



@api_view(http_method_names=['GET', 'POST'])
def homepage(request: Request):

    if request.method == 'POST':
        serializer = PostSerializer(data=request.data,many=True)

        if serializer.is_valid():
            serializer.save()

            return Response({
                'message': 'Post created successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({'message': 'Hello World!'})


class PostListCreateView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()

    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request: Request, *args, **kwargs):  # ← make sure this exists!
        return self.create(request, *args, **kwargs)




class PostRetrieveUpdateDeleteView(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self,request: Request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request: Request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request: Request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
