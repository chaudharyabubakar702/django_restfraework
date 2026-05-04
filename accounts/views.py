from django.shortcuts import render
from django.utils import dates

from accounts.serializers import SignUpSerializer
from rest_framework import  generics,status
from rest_framework.response import Response
from rest_framework.request import Request

# Create your views here.
class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer

    def post(self, request: Request) -> Response:
        date = request.data
        serializer = self.serializer_class(data=date)
        if serializer.is_valid():
            serializer.save()
            response={
                "message":"User created successfully",
                "data":serializer.data
            }
            return Response(data= response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)