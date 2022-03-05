from django.urls import path

from .views import v_post, index


urlpatterns = [
    path('', index.homepage, name="blog"),
    path('post', v_post.PostApiView.as_view(), name="post"),
    path('post/<str:uuid4>', v_post.PostApiView.as_view(), name="post")
    ]