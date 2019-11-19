from django.conf.urls import url
from . import views
from .views import (
Home, ViewPost, CreatePost,
UpdatePost,DeletePost, ViewProfile,
CreateComment,DeleteComment,
LikePostAPI, ViewLikes, ViewNotifications
)


urlpatterns = [
    url('', Home.as_view(), name='photo_blog-home'),
    url('search/', views.search, name='search'),
    url('post/<int:pk>/', ViewPost.as_view(), name='photo_blog-detail'),
    url('post/new/', CreatePost.as_view(), name='photo_blog-create'),
    url('post/<int:pk>/update', UpdatePost.as_view(), name='photo_blog-update'),
    url('post/<int:pk>/delete/', DeletePost.as_view(), name='photo_blog-delete'),
    url('user/<str:username>/', ViewProfile.as_view(), name='photo_blog-profile'),
    url('post/<int:pk>/comment/', CreateComment.as_view(), name='photo_blog-comment'),
    url('comment/<int:pk>/delete/', DeleteComment.as_view(), name='photo_blog-delete_comment'),
    url('post/<int:pk>/like_api/', LikePostAPI.as_view(), name='photo_blog-post_like_api'),
    url('post/<int:pk>/likes/', ViewLikes.as_view(), name='photo_blog-post_likes'),
    url('notifications/', ViewNotifications.as_view(), name='photo_blog-notifications'),
]
