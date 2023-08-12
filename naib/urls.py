from django.urls import path
from . import views

urlpatterns = [
    path('', views.naib, name='naib')
]
