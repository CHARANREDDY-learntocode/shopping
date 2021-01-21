from django.urls import path

from .views import ProductListView, ProductDetailView, ProductCreateView, ProductRetriveUpdateView

urlpatterns = [
    path('', ProductListView.as_view(), name= 'products-list'),
    path('<str:name>', ProductDetailView.as_view(), name= 'product-detail'),
    path('create/',  ProductCreateView.as_view(), name='create-product'),
    path('update/<str:name>', ProductRetriveUpdateView.as_view(), name= 'product-update-delete'),
]