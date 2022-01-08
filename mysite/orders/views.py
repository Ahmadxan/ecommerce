from django.shortcuts import render, redirect
from orders.forms import OrderForm
from orders.models import Order
from products.models import Product
from django.contrib.auth.decorators import login_required


def login_required_decorator(func):
    return login_required(func, login_url='login-page')


@login_required_decorator
def order_product(request, pk):
    product = Product.objects.get(id=pk)
    form = OrderForm(request.POST or None)
    if form.is_valid():
        form.instance.customer_id = request.user
        form.instance.product_id = product
        form.save()
        return redirect('checkout')
    return render(request, 'order/order.html', {'form': form})


@login_required_decorator
def checkout_page(request):
    return render(request, 'order/order-done.html')


@login_required_decorator
def my_order(request):
    orders = Order.objects.filter(customer_id=request.user)
    ctx = {
        'orders': orders
    }
    return render(request, 'order/order-list.html', ctx)
