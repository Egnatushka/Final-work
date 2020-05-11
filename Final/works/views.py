from django.shortcuts import render, redirect
from django.views import View

from .models import *
from .forms import *

from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    works = Work.objects.all()
    return render(request, 'works/work_example_list.html', context={'works': works})



class WorksDetail(LoginRequiredMixin, View):    
    def get(self, request, works_ex_id):
        work = Work.objects.get(id=works_ex_id)
        return render(request, 'works/work_detail.html', context={'work':work})

    raise_exception = True



class PriceList(View):

    def get(self, request):
        price_list = Price.objects.all()
        return render(request, 'works/price_list.html', context={'price_list': price_list})



class OrderList(View):

    def get(self, request):
        tag = Tag.objects.all()
        print(tag)
        return render(request, 'works/order_list.html', context={'tag': tag})



class OrderDetail(LoginRequiredMixin, View):
    def get(self, request, order_id):
        order = Order.objects.get(id=order_id)
        return render(request, 'works/order_detail.html', context={'order': order})

    raise_exception = True



class ActivDetailOrder(LoginRequiredMixin, View):
    def get(self, request, order_id):
        order = Order.objects.get(id=order_id)
        return render(request, 'works/active_order_detail.html', context={'order': order})

    raise_exception = True



class ComplitedOrderDetail(LoginRequiredMixin, View):
    def get(self, request, order_id):
        order = Order.objects.get(id=order_id)
        return render(request, 'works/complited_order_detail.html', context={'order': order})

    raise_exception = True



class ActivOrderList(View):

    def get(self, request):
        tag = Tag.objects.all()
        return render(request, 'works/activ_order.html', context={'tag': tag})



class ComplitedOrder(View):

    def get(self, request):
        tag = Tag.objects.all()
        return render(request, 'works/complited_order.html', context={'tag': tag})


class ComplitedOrderDelite(LoginRequiredMixin, View):
    
    def get(self, request, order_id):
        order = Order.objects.get(id=order_id)
        return render(request, 'works/complited_order_delite.html', context={'order': order})

    def post(self, request, order_id):
        order = Order.objects.get(id=order_id)
        order.delete()
        return redirect('complited_order_url')

    raise_exception = True



class OrderCreate(LoginRequiredMixin, View):

    def get(self, request):
        order = OrderForm(initial={'tag': Tag.objects.get(id=3)})
        return render(request, 'works/order_create.html', context={'order': order})

    def post(self, request):
        bound_form = OrderForm(request.POST)

        if bound_form.is_valid():
            new_order = bound_form.save()
            return redirect(new_order)
        return render(request, 'works/order_create.html', context={'order': bound_form})

    raise_exception = True



class OrderUpdate(LoginRequiredMixin, View):

    def get(self, request, order_id):
        order = Order.objects.get(id=order_id)
        bound_form = OrderUpdateForm(instance=order)
        return render(request, 'works/order_update.html', context={'form': bound_form, 'order': order})

    def post(self, request, order_id):
        order = Order.objects.get(id=order_id)
        bound_form = OrderUpdateForm(request.POST, instance=order)

        if bound_form.is_valid():
            if bound_form.cleaned_data['tag'].first() == Tag.objects.get(id=2):
                print("compited_order")
                new_order = bound_form.save()
                return redirect('complited_order_detail_url', order_id=order.id)
            new_order = bound_form.save()
            return redirect(new_order)
        return render(request, 'works/order_update.html', context={'form': bound_form, 'order': order})

    raise_exception = True