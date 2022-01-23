from django.urls import path

from . import views

urlpatterns = [ 
    path('content/login/', views.login, name='content.login'),
    # path('login/handle_login', views.handle_login, name='login.handle_login'),
    # path('login/validate/<str:token>/', views.validate, name='login.validate')
]
