from django.shortcuts import render
from django.contrib.auth import logout, authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, Group
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django_app import models
from django.urls import reverse


def home_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse(content=b"<h1>Hello World</h1>")

def post_list(request: HttpRequest) -> HttpResponse:
    posts = models.Post.objects.all()  # filter order_by
    context = {"posts": posts}
    return render(request, 'django_app/post_list.html', context=context)


def post_delete(request: HttpRequest, pk: int) -> HttpResponse:
    post = models.Post.objects.get(id=pk)
    post.delete()
    return redirect(reverse('django_app:post_list', args=()))

def post_create(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        context = {}
        return render(request, 'django_app/post_create.html', context=context)
    elif request.method == "POST":
        print("request: ", request)
        # print("request.data: ", request.data)
        print("request.POST: ", request.POST)
        print("request.GET: ", request.GET)
        print("request.META: ", request.META)

        title = request.POST.get('title', None)
        description = request.POST.get('description', "")
        post = models.Post.objects.create(
            title=title,
            description=description,
        )
        return redirect(reverse('django_app:post_list', args=()))
