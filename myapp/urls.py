from django.urls import path
from .views import get_items, create_item, hello_world

urlpatterns = [
    path("items/", get_items, name="get_items"),
    path("items/create/", create_item, name="create_item"),
    path(
        "hello/",
        hello_world,
    ),
]
