from django.shortcuts import render
from .models import *
from django.views import View




def index(request):
    works = Work.objects.all()
    return render(request, 'works/work_example_list.html', context={'works': works})



class WorksDetail(View):
    
    def get(self, request, works_ex_id):
        work = Work.objects.get(id=works_ex_id)
        return render(request, 'works/work_detail.html', context={'work':work})



class OrderList(View):

    def get(self, request):
        orders = Order.objects.all()
        return render(request, 'works/order_list.html', context={'orders': orders})



class OrderDetail(View):
    def get(self, request, order_id):
        order = Order.objects.get(id=order_id)
        return render(request, 'works/order_detail.html', context={'order': order})



class ActivOrderList(View):

    def get(self, request):
        tag = Tag.objects.all()
        return render(request, 'works/activ_order.html', context={'tag': tag})

