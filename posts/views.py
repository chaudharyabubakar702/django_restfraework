from rest_framework.request import Request
from rest_framework.response import  Response
from rest_framework import status, response
from rest_framework.decorators import api_view
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
@api_view(http_method_names=['GET','POST'])
def list_posts(request: Request):
    posts = Post.objects.all()
    if request.method == 'POST':
        data = request.data
        serializer = PostSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            response = {
                'message': 'Posts Created Success',
                'data': serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    serializer = PostSerializer(posts, many=True)
    response = {
        'message': 'Posts ',
        'data': serializer.data
    }

    return Response(response, status=status.HTTP_200_OK)


@api_view(http_method_names=['GET'])
def post_detail(request: Request,post_id: int):
    post = get_object_or_404(Post, id=post_id)
    serializer = PostSerializer(instance=post)
    response = {"message":"post","data":serializer.data}
    return Response(data=response, status=status.HTTP_200_OK)


# @api_view(http_method_names=['GET'])
# def get_post_by_id(request: Request,post_id: int):
#     pass


@api_view(http_method_names=['PUT'])
def update_post(request: Request,post_id: int):
    post = get_object_or_404(Post, id=post_id)
    data = request.data
    serializer = PostSerializer(instance=post,data=data)
    if serializer.is_valid():
        serializer.save()
        response = {
            'message': 'Post Updated Successfully',
            'data': serializer.data
        }
        return Response(data=response, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(http_method_names=['DELETE'])
def delete_post(request: Request,post_id: int):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)