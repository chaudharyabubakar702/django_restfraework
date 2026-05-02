from rest_framework.request import Request
from rest_framework.response import  Response
from rest_framework import status
from rest_framework.decorators import api_view


# 📌 Dummy posts data
posts = [
    {"id": 1,
     "title": "why python is difficult",
     "content": "This is to give reason why it is hard"
     },
    {"id": 2,
     "title": "Learn JavaScript",
     "content": "This is a course on js"
     }
]



@api_view(http_method_names=['GET', 'POST'])
def homepage (request: Request):
    if request.method == 'POST':
        data = request.data
        response = {'message': 'Hello World!', 'data': data}
        return Response(data = response, status = status.HTTP_201_CREATED)

    response =  {'message': 'Hello World!'}
    return Response(data=response , status=status.HTTP_200_OK)


@api_view(http_method_names=['GET'])
def list_posts(request: Request):
    return Response(data=posts, status=status.HTTP_200_OK)


@api_view(http_method_names=['GET'])
def post_detail(request: Request,post_index: int):
    post = posts[post_index]
    if post:
        return Response(data=post, status=status.HTTP_200_OK)

    return Response(data={"error":"Post not found"},status=status.HTTP_404_NOT_FOUND)