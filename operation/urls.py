from django.urls import path
from . import views

urlpatterns = [
    path('',views.operation_main ),
    path('cliente/', views.customer ),
]