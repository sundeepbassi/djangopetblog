"""Specify the URL patterns"""
from django.urls import path
from . import views

# Specify all the URL pattern logic, i.e. for each different URL
# specify the action we want to take, e.g. if the URL is /about
# then we should display the about page.
urlpatterns = [
    # Homepage (URL - /)
    path('', views.DisplayAllBlogPosts.as_view(), name='home'),

    # About page (URL - /about)
    path('about/', views.display_about_page, name='about'),

    # Gallery page (URL - /gallery)
    path('gallery/', views.display_gallery_page, name='gallery'),

    # Blog post (Example URL: /different-dog-breeds)
    path('<slug:slug>/', views.DisplayBLogPost.as_view(), name='post_detail'),

    # Like a blog post (Example URL: /like/different-dog-breeds)
    path('like/<slug:slug>', views.LikeBlogPost.as_view(), name='post_like'),

    # Edit a blog post comment (Example URL: /comment/edit/15)
    path('comment/edit/<int:pk>',
         views.UpdateBlogPostComment.as_view(),
         name='update_comment'),

    # Delete a blog post comment (Example URL: /comment/delete/15)
    path('comment/delete/<int:pk>',
         views.DeleteBlogPostComment.as_view(),
         name='delete_comment'),
]
