from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:blog_id>/', views.detail, name= 'detail'),
    path('new/', views.new, name= 'new'),
    path('<int:blog_id>/delete/', views.delete, name='delete'),
    path('<int:blog_id>/edit/', views.edit, name='edit'),
    path('<int:blog_id>/update/', views.update, name='update'),
    path('<int:blog_id>/comments/', views.add_comment, name='add_comment'),
    path('edit_comment/<int:blog_id>/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),

]