from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from demonstration.views import Views


urlpatterns = [
    path(r'admin/', admin.site.urls),
    url(r'^$', Views.home, name='home')
]
