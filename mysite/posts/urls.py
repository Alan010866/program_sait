from django.urls import path
from .views import view_posts

urlpatterns = [
    path('', view_posts)
]
