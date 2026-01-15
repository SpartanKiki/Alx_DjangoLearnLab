from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post-list'),
    path('register/', views.register, name='register'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),

    path('post/<int:pk>/comments/new/', views.comment_create, name='comment-create'),
    path('comment/<int:pk>/update/', views.comment_update, name='comment-update'),
    path('comment/<int:pk>/delete/', views.comment_delete, name='comment-delete'),

    path('search/', views.post_search, name='post-search'),
]
# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # ... your existing paths ...
    path('search/', views.search_posts, name='search-posts'),
    path('tags/<str:tag_name>/', views.search_posts, name='posts-by-tag'),
]
