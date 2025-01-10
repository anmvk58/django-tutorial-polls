from django.urls import path
from . import views

urlpatterns = [
    path("", views.list_all_post, name="index"),
    path("<int:id>", views.list_one_post, name="index")
]