# Urls related to an account

from django.conf import settings
from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy

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
    path('change-password/',
         auth_views.PasswordChangeView.as_view(
             template_name='main/generic_form.html',
             success_url=reverse_lazy('account:logout'),
             extra_context={
                 'title': acc_const.CHANGE_PASSWORD_TITLE,
             },
         ),
         name='change_password'),
    path('profile/', acc_views.profile, name='profile'),
    path('delete-account/', acc_views.delete_account, name='delete_account'),
    path('edit-profile/', acc_views.edit_profile, name='edit_profile'),
    path('list/<int:vehicle>/', acc_views.list_vehicle, name='list_vehicle'),
    path('delete-all-listings/', acc_views.delete_all_listings, name='delete_all_listings'),
    path('delete-listing/<int:listing>/', acc_views.delete_listing, name='delete_listing'),
]
