from django.urls import path
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views
# from django.contrib.auth.views import

urlpatterns = [
    path('register/', accounts_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    # path('login/', accounts_views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('index/', accounts_views.index, name='index')
]
