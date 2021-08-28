from django.contrib import admin
from django.urls import path, include

from store import views

urlpatterns = [
    path('product/list/', views.ProductView.as_view(), name='product_list'),
    path('product/create/', views.CreateProductView.as_view(), name='product_create'),
    path('product/detail/<int:pk>/', views.DetailProductView.as_view(), name='product_detail'),
    path('product/modify/<int:pk>/', views.ModifyProductView.as_view(), name='product_modify'),
    path('product/delete/<int:pk>/', views.DeleteProductView.as_view(), name='product_delete'),

    path('producent/list/', views.ProducentView.as_view(), name='producent_list'),
    path('producent/create/', views.CreateProducentView.as_view(), name='producent_create'),
    path('producent/modify/<int:pk>/', views.ProducentDetailView.as_view(), name='producent_modify'),

    path('category/list/', views.CategoryView.as_view(), name='category_list'),
    path('category/create/', views.CreateCategoryView.as_view(), name='category_create'),
    path('category/modify/<int:pk>/', views.ModifyCategoryView.as_view(), name='category_modify'),
    path('category/delete/<int:pk>/', views.DeleteCategoryView.as_view(), name='category_delete'),

    path('order/list/', views.OrderView.as_view(), name='order_list'),
    path('order/create/', views.CreateOrderView.as_view(), name='order_create'),
    path('order/detail/<int:pk>/', views.DetailOrderView.as_view(), name='order_detail'),

    path('opinion/list/', views.OpinionView.as_view(), name='opinion_list'),
    path('opinion/create/', views.CreateOpinionView.as_view(), name='opinion_create'),

    path('basket/list/', views.BasketView.as_view(), name='basket_list'),
    path('add_to_basket/', views.AddProductToBasket.as_view(), name='add_to_basket'),
    path('basket/delete/<int:pk>/', views.DeleteBasketProductView.as_view(), name='basket_delete'),
]