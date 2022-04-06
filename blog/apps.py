"""This module is used for application configuration"""
from django.apps import AppConfig


class BlogConfig(AppConfig):
    """This class is the configuration for the blog"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
