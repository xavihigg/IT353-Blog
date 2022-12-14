from . import views
from .models import Post
from django.urls import path

urlpatterns = [
    path('register/', views.Register, name="register"),   
    path('login/', views.my_login_view, name="login"),
	path('logout/', views.my_logout_view, name="logout"),
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
] 
