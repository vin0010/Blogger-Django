"""blogger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url

import posts
from .views import (posts_create,
                    posts_delete,
                    posts_detail,
                    posts_list,
                    posts_update)

urlpatterns = [
    # url(r'^$', "posts.views.posts_list"),
    url(r'^$', posts_list),
    # url(r'^create', "posts.views.posts_create"),
    url(r'^create', posts_create),
    # url(r'^update', "posts.views.posts_update"),
    url(r'^update', posts_update),
    # url(r'^detail', "posts.views.posts_detail"),
    url(r'^detail', posts_detail),
    # url(r'^delete', "posts.views.posts_delete"),
    url(r'^delete', posts_delete),
]
