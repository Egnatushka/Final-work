from django.urls import path
from .views import *


urlpatterns = [
    path('example/', index, name='work_example_list'),
    path('example/<int:works_ex_id>/', WorksDetail.as_view(), name='works_detail_url'),
    path('orders/', OrderList.as_view(), name='order_list_url'),
    path('orders/create/', OrderCreate.as_view(), name='order_crate_url'),
    path('orders/<int:order_id>/', OrderDetail.as_view(), name='order_detail_url'),
    path('active/', ActivOrderList.as_view(), name='active_order_url'),

]