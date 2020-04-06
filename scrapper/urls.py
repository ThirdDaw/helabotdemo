from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("action/", views.action, name='action'),
    path("action/preview/<path:path>", views.preview, name='preview')
]
