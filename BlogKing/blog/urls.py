from . import views
from .models import Post
from django.urls import path

urlpatterns = [
    path('register/', views.Register, name="register"),   
    path('login/', views.my_login_view, name="login"),
	path('logout/', views.my_logout_view, name="logout"),
    path('post_create/', views.PostCreateForm.as_view(), name='post_create'),
    path('', views.PostList.as_view(), name='home'),
    path('home/', views.PostList.as_view(), name='home'),
    path('post_detail/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('post_edit/<slug:slug>/', views.PostEditForm.as_view(), name='post_edit'),
    path('post_delete/<slug:slug>/', views.PostDeleteForm.as_view(), name='post_delete'),
    
] 
