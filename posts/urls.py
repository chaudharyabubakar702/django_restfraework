from . import views
from django.urls import path

urlpatterns = [
    path("homepage/", views.homepage, name="posts_home"),
    path("", views.PostListCreateView.as_view(), name="PostListCreateView"),
    path("<int:pk>/", views.PostRetrieveUpdateDeleteView.as_view(), name="PostRetrieveUpdateDeleteView"),
]