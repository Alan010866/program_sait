from django.urls import path
from .views import create_post, view_posts, autor

urlpatterns = [
    path('', view_posts, name="main"),
    path("create/", create_post, name="create"),
    path("autor/", autor, name="autor")
]
