from django.shortcuts import render, redirect
from django.views import View

from .models import *
from .forms import *



def index(request):
    info = Info.objects.all()
    works = Work.objects.all()
    return render(request, 'works/work_example_list.html', context={'works': works, 'info': info})



class WorksDetail(View):    
    def get(self, request, works_ex_id):
        work = Work.objects.get(id=works_ex_id)
        return render(request, 'works/work_detail.html', context={'work':work})



class PriceList(View):

    def get(self, request):
        price_list = Price.objects.all()
        return render(request, 'works/price_list.html', context={'price_list': price_list})



class OrderList(View):

    def get(self, request):
        # orders = Order.objects.all()
        # return render(request, 'works/order_list.html', context={'orders': orders})

        tag = Tag.objects.all()
        return render(request, 'works/order_list.html', context={'tag': tag})



class OrderDetail(View):
    def get(self, request, order_id):
        order = Order.objects.get(id=order_id)
        return render(request, 'works/order_detail.html', context={'order': order})



class ActivDetailOrder(View):
    def get(self, request, order_id):
        order = Order.objects.get(id=order_id)
        return render(request, 'works/active_order_detail.html', context={'order': order})



class ComplitedOrderDetail(View):
    def get(self, request, order_id):
        order = Order.objects.get(id=order_id)
        return render(request, 'works/complited_order_detail.html', context={'order': order})



class ActivOrderList(View):

    def get(self, request):
        tag = Tag.objects.all()
        return render(request, 'works/activ_order.html', context={'tag': tag})



class ComplitedOrder(View):

    def get(self, request):
        tag = Tag.objects.all()
        return render(request, 'works/complited_order.html', context={'tag': tag})


class ComplitedOrderDelite(View):
    
    def get(self, request, order_id):
        order = Order.objects.get(id=order_id)
        return render(request, 'works/complited_order_delite.html', context={'order': order})

    def post(self, request, order_id):
        order = Order.objects.get(id=order_id)
        order.delete()
        return redirect('complited_order_url')



class OrderCreate(View):

    def get(self, request):
        order = OrderForm(initial={'tag': Tag.objects.get(id=3)})
        return render(request, 'works/order_create.html', context={'order': order})

    def post(self, request):
        bound_form = OrderForm(request.POST)

        if bound_form.is_valid():
            new_order = bound_form.save()
            return redirect(new_order)
        return render(request, 'works/order_create.html', context={'order': bound_form})



class OrderUpdate(View):

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