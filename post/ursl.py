from django.urls import path
from .views import BlogListCreateView, BlogDetailView, MyBlogsView, CommentCreateView

urlpatterns = [
   
    path('blogs/', BlogListCreateView.as_view(), name='blog-list'),
    
   
    path('blogs/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
    
   
    path('my-blogs/', MyBlogsView.as_view(), name='my-blogs'),
    
  
    path('blogs/<int:pk>/comment/', CommentCreateView.as_view(), name='comment-create'),
]
