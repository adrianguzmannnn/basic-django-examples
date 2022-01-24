"""The views for the content service."""
import http
import uuid
import requests
from django.shortcuts import redirect
from django.http import HttpResponse, QueryDict
from django.core import serializers
from django.views.decorators.http import require_http_methods
from django.core.handlers.wsgi import WSGIRequest
from LoginService.models import User
from ContentService.models import Patient


@require_http_methods(["GET"])
def content_login(request: WSGIRequest) -> HttpResponse:
    token = request.session.get("token")
    if token == User.objects.get(username="tonystark",
                                 password="ironman123").expected_token:
        return HttpResponse(content="You are already signed in.", status=http.HTTPStatus.OK)
    return redirect("/login/")


@require_http_methods(["PUT"])
def authenticate(request: WSGIRequest) -> HttpResponse:
    request.session["token"] = QueryDict(request.body).get("token")
    return HttpResponse(status=http.HTTPStatus.OK)


@require_http_methods(["PUT"])
def logout(request: WSGIRequest) -> HttpResponse:
    if "token" in request.session:
        request.session.pop("token")
    return HttpResponse(status=http.HTTPStatus.OK)


@require_http_methods(["GET"])
def case_guid(request: WSGIRequest, guid: uuid.uuid4) -> HttpResponse:
    if request.session.get("token"):
        ping = requests.get(url=f"http://{request.get_host()}/validate/{request.session.get('token')}")
        if ping.status_code == http.HTTPStatus.OK:
            try:
                patient = Patient.objects.get(case_uuid=guid) 
            except Patient.DoesNotExist:
                return HttpResponse(status=http.HTTPStatus.UNAUTHORIZED)
            else:
                return HttpResponse(content=serializers.serialize("json", [patient,]), status=http.HTTPStatus.OK) 
    return HttpResponse(status=http.HTTPStatus.UNAUTHORIZED)


@require_http_methods(["GET"])
def case_age(request: WSGIRequest, age: int, operation: str) -> HttpResponse:
    if request.session.get("token"):
        ping = requests.get(url=f"http://{request.get_host()}/validate/{request.session.get('token')}")
        if ping.status_code == http.HTTPStatus.OK:
            try:
                if operation == "eq":
                    patients = Patient.objects.filter(age=age)
                elif operation == "gt":
                    patients = Patient.objects.filter(age__gt=age)
                elif operation == "lt":
                    patients = Patient.objects.filter(age__lt=age)
                elif operation == "ge":
                    patients = Patient.objects.filter(age__gte=age)
                elif operation == "le":
                    patients = Patient.objects.filter(age__lte=age)
            except Patient.DoesNotExist:
                return HttpResponse(status=http.HTTPStatus.UNAUTHORIZED)
            else:
                return HttpResponse(content=serializers.serialize("json", patients), status=http.HTTPStatus.OK) 
    return HttpResponse(status=http.HTTPStatus.UNAUTHORIZED)
