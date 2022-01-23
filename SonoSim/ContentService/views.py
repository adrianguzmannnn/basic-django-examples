import http
from django.shortcuts import render, redirect
from LoginService.models import User
from django.http import HttpResponse

# Create your views here.

def login(request):
    token = request.session.get("token")
    if token and token == User.objects.get(username="tonystark", password="ironman123").expected_token:
        return HttpResponse(content="You are already signed in.", status=http.HTTPStatus.OK)
    return redirect("/login/")

def authenticate(request):
    request.session.update({"token": request.PUT.get("token")})

def logout(request):
    request.session.pop("token")

def case(request, guid):
    if request.session.get("token") == User.objects.get(username="tonystark", password="ironman123").expected_token:
        try:
            User.objects.get(case_uuid=guid)
