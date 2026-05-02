from urllib import response

from django.shortcuts import render
from django.http import HttpRequest,JsonResponse

# Create your views here.
def homepage(request: HttpRequest):
    response = {"message": "Hello World"}
    return JsonResponse(response)
