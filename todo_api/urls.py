from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.getTODOs),
    path('users/', views.getUsers),
    path('login/', views.login),
    path('post/', views.postTODO),
    path('completeTODO/', views.markTODOAsComplete),
]
