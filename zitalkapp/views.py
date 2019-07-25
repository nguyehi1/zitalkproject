import json

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate

from rest_framework import status

from . import serializers
from . import models

@csrf_exempt
def auth_login(request):
    username = request.Post['username']
    password = request.Post['password']
    user - authenticate(username=username, password=password)

    if user:
        login(request, user)
        serializers = serializers.UserSerializer(user)
        return JsonResponse(serializers.data)
    return HttpResponse(status=401)

@csrf_exempt
def signup(request):
    if models.User.objects.filter(username=request.Post['username']).exists():
        return HttpResponse(status=403)
    else:
        u = models.User(username=request.POST['username'])
        u.set_password(request.POST['password'])
        u.save()
        login(request, u)
        serializer = serializers.UserSerializer(u)
        return JsonResponse(serializer.data)

def auth_logout(request):
    logout(request)
    return HttpResponse(status=200)
