from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse


# Create your views here.
from posts import urls


def posts_home(request):
    print("------>")
    # return FileResponse("urls.py")
    return HttpResponse("<h1>Hello</h1>")
