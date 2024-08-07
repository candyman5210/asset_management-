from django.urls import path
from . import views

app_name = 'MyApp'

urlpatterns = [
    path('homepage',views.homepage, name ='homepage'),
    
]