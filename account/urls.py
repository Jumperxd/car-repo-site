# Urls related to an account

from django.urls import path

from . import views, forms

app_name = 'account'
urlpatterns = [
    path('signup/', views.create_user, name='signup'),
]
