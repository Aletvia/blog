from django.urls import path

from .views import v_post


urlpatterns = [
    path('', v_post.PostApiView.as_view(), name="post"),
    path('<str:uuid4>', v_post.PostApiView.as_view(), name="post")
    ]