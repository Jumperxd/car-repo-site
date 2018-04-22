# Urls related to an account

from django.conf import settings
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views as acc_views, constants as acc_const

app_name = 'account'
urlpatterns = [
    path('signup/', acc_views.create_user, name='signup'),
    path('login/',
         auth_views.LoginView.as_view(
             template_name='account/login.html',
             extra_context={
                 'title': acc_const.LOGIN_TITLE,
                 'submit': 'Login',
                 'debug': settings.DEBUG,
             },
             redirect_authenticated_user=True,
         ),
         name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', acc_views.profile, name='profile'),
    path('list/<int:vehicle>/', acc_views.list_vehicle, name='list_vehicle'),
]
