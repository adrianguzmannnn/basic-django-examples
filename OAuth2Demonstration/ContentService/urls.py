from django.urls import path

from . import views

urlpatterns = [
    path('content/login/', views.content_login, name='content_login'),
    path('content/authenticate/', views.authenticate, name='authenticate'),
    path('content/logout/', views.logout, name='logout'),
    path('content/case/<uuid:guid>', views.case_guid, name='case_guid'),
    path('content/case/<int:age>/<str:operation>', views.case_age, name='case_age')
]
