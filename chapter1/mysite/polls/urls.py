from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("<int:question_id>", views.detail, name="detail"),
    path("<ing:question_id>", views.results, name="results"),
    path("<int:question_id>",views.vote,name="vote"),
    
]
