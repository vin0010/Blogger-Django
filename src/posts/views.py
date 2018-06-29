from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import FileResponse

# Create your views here.
from posts import urls
from .models import Post

def posts_list(request):
    print("------>")
    # instance = Post.objects.get(id=100)
    queryset = Post.objects.all()
    result = ""
    for obj in queryset:
        result += obj.title + "\n"
    context = {}
    if request.user.is_authenticated():
        context = {
            "Detail": result,
            "myqueryset": queryset,
            "Name": "Vinoth",
            "Designation": "Software Engineer"
        }
    else:
        context = {
            "Detail": "Authentication failed for List",
            "Name": "Vinoth",
            "Designation": "Software Engineer"
        }
    return render(request, "index.html", context)
    # return HttpResponse("<h1>List</h1>")


def posts_create(request):
    if request.user.is_authenticated():
        context = {
            "Detail": "Create",
        }
    else:
        context = {
            "Detail": "Create",
        }
    print("------>")
    # return HttpResponse("<h1>Create</h1>")
    return render(request, "index.html", context)


def posts_update(request):
    print("------>")
    if request.user.is_authenticated():
        context = {
            "Detail": "Update",
        }
    # return HttpResponse("<h1>Update</h1>")
    return render(request, "index.html", context)


def posts_detail(request):
    instance = get_object_or_404(Post, id="1")
    print("------>", instance.id)
    context = {
        "Detail": "Detail",
        "myqueryset" : instance,
    }
    # return HttpResponse("<h1>Detail</h1>")
    return render(request, "post_detail.html", context)


def posts_delete(request):
    print("------>")
    context = {
        "Detail": "Delete",
    }
    # return HttpResponse("<h1>Delete</h1>")
    return render(request, "index.html", context)
