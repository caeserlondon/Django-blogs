from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostUpdateView, PostDeleteView, DraftListView, add_comment_to_post, comment_approve, comment_remove, post_publish



urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/new', views.CreatePostView.as_view(), name='post_new'),
    path('posts/<int:pk>/', PostUpdateView.as_view(), name='post_edit'),
    path('posts/<int:pk>/delete', PostDeleteView.as_view(), name='post_remove'),
    path('drafts/', DraftListView.as_view(), name='post_draft_list'),
    path('posts/<int:pk>/coment/', add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', comment_remove, name='comment_remove'),

    path('posts/<int:pk>/publish', post_publish, name='post_publish'),
]