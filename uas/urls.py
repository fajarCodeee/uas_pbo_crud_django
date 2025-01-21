from django.urls import path
from . import views

app_name = 'uas'
urlpatterns = [
    # Task URLs
    path('', views.index_view, name='index'),
    path('<int:task_id>', views.detail_view, name='detail'),
    path('create', views.create_view, name='create'),
    path('update/<int:task_id>', views.update_view, name='update'),
    path('delete/<int:task_id>', views.delete_view, name='delete'),
    
    # Category URLs
    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/<int:category_id>/', views.category_detail, name='category_detail'),
    path('categories/<int:category_id>/update/', views.category_update, name='category_update'),
    path('categories/<int:category_id>/delete/', views.category_delete, name='category_delete'),
    
    # Comment URLs
    path('task/<int:task_id>/comment/add/', views.comment_create, name='comment_create'),
    path('comment/<int:comment_id>/update/', views.comment_update, name='comment_update'),
    path('comment/<int:comment_id>/delete/', views.comment_delete, name='comment_delete'),
]