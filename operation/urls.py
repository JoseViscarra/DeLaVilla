from django.urls import path
from . import views

urlpatterns = [
    path('',views.operation_main, name='home' ),
    path('customer/', views.customer, name='customer' ),
]