from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("add", views.addItem, name = "add"),
    path("complete/<item_id>", views.completeItem, name = "complete"),
    path("deleteitem/<item_id>", views.deleteItem, name = "deleteitem"),
    path("deleteall", views.deleteAll, name = "deleteall"),
]
