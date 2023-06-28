from django.urls import path
from .views import *

urlpatterns = [
    path('test/', Test.as_view()),
    path('posts/', Posts.as_view()),
    path('all-posts/', AllPosts.as_view()),
    path('create-post/', CreatePost.as_view()),
    path('detail-post/<int:pk>/', PostDetail.as_view()),
    path('update-post/<int:pk>', UpdatePost.as_view()),
    path('delete-post/<int:pk>', DeletePost.as_view()),
    path('form/', PostFormView.as_view()),
    path('input-form/', InputFormView.as_view()),
]