from django.urls import path

from . import views
app_name = "wiki"
urlpatterns = [
    path("", views.index, name="index"),
    path ("wiki/<str:title>", views.entry, name="entry"),
    path("search", views.search, name="search"),
    path("new", views.new, name="new"),
    path("addNew", views.addNew, name="addNew"),
    path("edit" , views.edit, name="edit"),
    path("saveEdit", views.saveEdit, name="saveEdit")
]
