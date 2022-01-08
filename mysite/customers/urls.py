from django.urls import path
from . import views

urlpatterns = [
    path('user/create/', views.SignUp.as_view(), name='signup'),
    path('login/', views.login_page, name='login-page'),
    path('logout/', views.logout_page, name='logout-page'),
]
