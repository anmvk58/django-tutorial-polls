from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    # 3 line for method 1
    # path("", views.index, name="index"),
    # path("<int:question_id>/", views.detail, name="detail"),
    # path("<int:question_id>/results/", views.results, name="results"),
    # 3 line for method 2
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]