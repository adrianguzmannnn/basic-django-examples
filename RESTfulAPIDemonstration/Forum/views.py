from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse


@require_http_methods(["GET"])
def chess(request: WSGIRequest) -> HttpResponse:
    return render(request, 'chess.html', {})
