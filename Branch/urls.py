from django.urls import path
from . import views

urlpatterns = [
    path('branch',views.branch, name = "branch")
]
