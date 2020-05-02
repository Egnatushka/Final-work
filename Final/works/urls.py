from django.urls import path
from .views import *


urlpatterns = [
    path('example/', index, name='work_example_list'),
    path('example/<int:works_ex_id>/', WorksDetail.as_view(), name='works_detail_url'),

]