from django.urls import path 

from .views import (CategoryListView, CategoryDetailView,
                    ProductListView, ProductDetailView,
                    )


urlpatterns = [
    
    path('categories/', CategoryListView.as_view(), name= 'Category list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name= 'Category detail'),
    
    path('products/', ProductListView.as_view(), name='Product list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='Product detail')
]
