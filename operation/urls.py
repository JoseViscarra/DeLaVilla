from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard, name='dashboard' ),
    path('production/', views.production, name='production'),
    path('orders/', views.orders, name='orders'),
    path('customer/', views.customer, name='customer' ),
]