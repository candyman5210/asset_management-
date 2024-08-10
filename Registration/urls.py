from django.urls import path
from . import views

app_name = 'registration'

urlpatterns = [
    path('registration',views.registration, name='registration'),
    path('login',views.login,name='login'),
    path('sign_out',views.sign_out,name='sign_out')
]