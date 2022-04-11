"""Specify the URL patterns"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('about/', views.About, name='about'),
    path('gallery/', views.Gallery, name='gallery'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('comment/edit/<int:pk>',
         views.UpdateCommentView.as_view(),
         name='update_comment'),
    path('comment/delete/<int:pk>',
         views.DeleteCommentView.as_view(),
         name='delete_comment'),
]
