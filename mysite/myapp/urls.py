from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("upload", views.uploader, name="upload"),
    path("post_created", views.post_create, name="posted")
]
