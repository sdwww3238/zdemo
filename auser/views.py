from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('hello,这是第一次用djongo写项目,yeah')