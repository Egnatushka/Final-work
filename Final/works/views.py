from django.shortcuts import render
from .models import *
from django.views import View

def index(request):
    works = Work.objects.all()
    return render(request, 'works/work_example_list.html', context={'works':works})

class WorksDetail(View):
    
    def get(self, request, works_ex_id):
        work = Work.objects.get(id=works_ex_id)
        return render(request, 'works/work_detail.html', context={'work':work})

