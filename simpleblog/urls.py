from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter

from posts.views import PostViewSet



router = DefaultRouter()
router.register('', PostViewSet, basename='post')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include(router.urls)),
    path("auth/",include("accounts.urls")),
]

