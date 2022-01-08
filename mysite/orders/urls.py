from django.urls import path

from . import views

urlpatterns = [
    path('product/<int:pk>/order/', views.order_product, name='order'),
    path('product/order/checkout/', views.checkout_page, name='checkout'),
    path('order/my-orders/', views.my_order, name='my-order'),
    # path('product/<int:pk>/order/', views.OrderCreateView.as_view(), name='order')
]