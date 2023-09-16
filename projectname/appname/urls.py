from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('posts/', views.post_list, name='post_list'),
    path('create_posts/', views.create_post, name='create_posts'),
    path('home', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='appname/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.home, name='home'),
    path('email/', views.send_newsletter, name='send_email'),
    path('view_posts/', views.view_posts, name='view_posts'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/update/', views.update_post, name='update_post'),
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),
    
]

from django.conf import settings
from django.conf.urls.static import static



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
