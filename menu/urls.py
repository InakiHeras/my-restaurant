from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('menu/', views.menu, name='menu'),
    path('menu/details/<int:id>', views.details, name='details'),
    path('my_orders/', views.myOrders, name='my_orders'),
    path('my_orders/create_order/', views.createOrder, name='create_order'),
    path('my_orders/update_order/<str:pk>/', views.updateOrder, name='update_order'),
    path('my_orders/delete_order/<str:pk>/', views.deleteOrder, name='delete_order'),
]