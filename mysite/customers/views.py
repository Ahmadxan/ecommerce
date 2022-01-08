from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth import login, logout, authenticate
from customers.forms import CustomUserCreationForm, CustomUserChangeForm
from customers.models import CustomUser


class SignUp(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home-page')


def login_page(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('home-page')
    return render(request, 'registration/login.html')


def logout_page(request):
    logout(request)
    return redirect('home-page')


#
# class CustomUserChangeView(UpdateView):
#     model = CustomUser
#     template_name = 'product/checkout.html'
#     form_class = CustomUserChangeForm
#     success_url = reverse_lazy('home-page')
