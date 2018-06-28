from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse


# Create your views here.
from posts import urls


def posts_list(request):
    print("------>")
    return HttpResponse("<h1>List</h1>")

def posts_create(request):
    print("------>")
    return HttpResponse("<h1>Create</h1>")

def posts_update(request):
    print("------>")
    return HttpResponse("<h1>Update</h1>")

def posts_detail(request):
    print("------>")
    return HttpResponse("<h1>Detail</h1>")

def posts_delete(request):
    print("------>")
    return HttpResponse("<h1>Delete</h1>")
