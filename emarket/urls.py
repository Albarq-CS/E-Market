from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.list_products, name='list_products'),
    path('products/add/', views.add_product, name='add_product'),
    path('products/<int:pk>/', views.view_product, name='view_product'),
    path('products/<int:pk>/delete/', views.delete_product, name='delete_product'),
    path('search/', views.search_categories, name='search_categories'),
]