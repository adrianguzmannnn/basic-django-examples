"""The views for the login service."""
import http
import uuid
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.core.handlers.wsgi import WSGIRequest
from .models import User


@require_http_methods(["GET"])
def login(request: WSGIRequest) -> HttpResponse:
    return render(request, 'login.html', {})


@require_http_methods(["POST"])
def handle_login(request: WSGIRequest) -> HttpResponse:
    try:
        user = User.objects.get(username=request.POST.get("Username"),
                                password=request.POST.get("Password"))
    except User.DoesNotExist:
        return HttpResponse(content='The credentials do not match.',
                            status=http.HTTPStatus.UNAUTHORIZED)
    else:
        # import requests
        # requests.put(url=f"http://{request.get_host()}/content/authenticate/",
        #              data={"token": user.expected_token})
        request.session["token"] = user.expected_token
        return HttpResponse(content="You have successfully signed in.", status=http.HTTPStatus.OK)


@require_http_methods(["GET"])
def validate(request: WSGIRequest, token: uuid.uuid4) -> HttpResponse:
    if token == User.objects.get(username="tonystark", password="ironman123").expected_token:
        return HttpResponse(content="Success.", status=http.HTTPStatus.OK)
    return HttpResponse(content='Failure.', status=http.HTTPStatus.UNAUTHORIZED)
