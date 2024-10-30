from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name = "home"),
    path("get_res/<int:pk>/", get_res, name="get_res"),
    path("add_res/", add_res, name="add_res"),
    path("upd_res/<int:pk>/", upd_res, name="upd_res"),
    path("del_res/<int:pk>/", del_res, name="del_res"),
    path("reviews/<int:pk>/", reviews, name="reviews"),
    path("add_review/", add_review, name="add_review"),
]
