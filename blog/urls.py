from django.urls import path
from django.views import (
    create_blog_view,
)

appname = 'blog'


urlpatters = [
    path('create/', create_blog_view, name='create')
]
