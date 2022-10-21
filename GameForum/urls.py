from django.urls import path

from GameForum.views import home

urlpatterns = [
    path('', home),
]
