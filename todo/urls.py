from django.urls import path
from . import views
from django.views.generic import CreateView
from django.urls import reverse_lazy

urlpatterns = [
    path("", views.list_view, name="list-view"),
    path("create/", views.create_view, name="create-view"),
    path("<id>", views.detail_view, name="detail-view"),
    path("update/<id>", views.update_view, name="update-view"),
    path("delete/<id>", views.delete_view, name="delete-view"),
]
