from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("new_page", views.new_page, name="new_page"),
    path("add_page", views.add_page, name="add_page"),
    path("edit_page/<str:title>", views.edit_page, name="edit_page"),
    path("modify_page/<str:title>", views.modify_page, name="modify_page"),
    path("random_page", views.random_page, name="random_page"),
    path("<str:title>", views.view_post, name ="view_post")
]

