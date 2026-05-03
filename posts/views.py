from rest_framework.request import Request
from rest_framework.response import  Response
from rest_framework import status, response
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


class PostListCreateView(APIView):
    serializer_class = PostSerializer
    def get(self,request:Request,*args,**kwargs):
        posts = Post.objects.all()
        serializer = self.serializer_class(instance=posts,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def post(self,request:Request,*args,**kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'message': 'Post created successfully',
                'data': serializer.data
            }
            return Response(data=response,status=status.HTTP_201_CREATED)




class PostRetrieveUpdateDeleteView(APIView):
    serializer_class = PostSerializer
    def get (self,request:Request,post_id:int):
        post = get_object_or_404(Post,pk=post_id)
        serializer = self.serializer_class(instance=post)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def put(self,request:Request,post_id:int):
        post = get_object_or_404(Post,pk=post_id)
        serializer = self.serializer_class(instance=post,data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'message': 'Post updated successfully',
                'data': serializer.data
            }
            return Response(data=response,status=status.HTTP_200_OK)

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request:Request,post_id:int):
        post = get_object_or_404(Post,pk=post_id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)










