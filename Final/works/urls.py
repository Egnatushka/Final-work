from django.urls import path
from .views import *


urlpatterns = [
    path('example/', index, name='work_example_list'),
    path('example/<int:works_ex_id>/', WorksDetail.as_view(), name='works_detail_url'),
    path('price/', PriceList.as_view(), name='price_list_url'),
    path('orders/', OrderList.as_view(), name='order_list_url'),
    path('orders/create/', OrderCreate.as_view(), name='order_crate_url'),
    path('orders/<int:order_id>/', OrderDetail.as_view(), name='order_detail_url'),
    path('orders/<int:order_id>/update', OrderUpdate.as_view(), name='order_update_url'),
    path('active/', ActivOrderList.as_view(), name='active_order_url'),
    path('active/detail/<int:order_id>', ActivDetailOrder.as_view(), name='active_order_detail_url'),
    path('complited/', ComplitedOrder.as_view(), name='complited_order_url'),
    path('complited/detail/<int:order_id>', ComplitedOrderDetail.as_view(), name='complited_order_detail_url'),
    path('complited/detail/<int:order_id>/delite', ComplitedOrderDelite.as_view(), name='complited_order_delite_url'),

]