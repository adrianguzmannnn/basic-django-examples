"""The views for the login service."""
import http
import requests
from django.shortcuts import render
from django.http import HttpResponse
from .models import User


def login(request):
    """A route for the login page."""
    return render(request, 'login.html', {})

def handle_login(request):
    """A route for the login page."""
    # print(request.get_host())
    try:
        user = User.objects.get(username=request.POST.get("Username"), password=request.POST.get("Password"))
    except User.DoesNotExist:
        return HttpResponse(content='The credentials do not match for any user.', status=http.HTTPStatus.UNAUTHORIZED)
    else:
        requests.put(url="/content/authenticate", data={"token": user.expected_token})
        return HttpResponse(content="You have successfully signed in.", status=http.HTTPStatus.OK)

def validate(request, token):
    if token == User.objects.get(username="tonystark", password="ironman123").expected_token:
        return HttpResponse(content="Success.", status=http.HTTPStatus.OK)
    return HttpResponse(content='Failure.', status=http.HTTPStatus.UNAUTHORIZED)
