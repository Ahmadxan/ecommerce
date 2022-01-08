from django.urls import path

from products.views import home_page, product_detail

urlpatterns = [
    path('', home_page, name='home-page'),
    path('product/<int:pk>/detail/', product_detail, name='product-detail'),
]