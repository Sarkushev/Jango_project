from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_post, name='create_post'),
    path('edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('login/', views.login_view, name='login'),
    path('', views.post_list, name='post_list'),  # список постов на /blog/
]