from queue import Empty
from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from django.views import View

from load_data.models import ReadCSV

import json

from visualization.forms import EditReadCSVForm
# Create your views here.

class TableView(View):
    template_name = 'visualization/index.html'
    
    def get(self, request, *args, **kwargs):


        everything = ReadCSV.objects.all()
        allTradecode = list(dict.fromkeys(list(everything.values_list('trade_code', flat=True))))

        p = Paginator(everything, 27)
        page_number = request.GET.get('page')
        try:
            page_obj = p.get_page(page_number)
        except PageNotAnInterger:
            page_obj = p.page(1)
        except EmptyPage:
            page_obj = p.page(p.num_pages)

        
        masterDict = {}

        for code in allTradecode:
            masterDict[code] = {
                'date': list(everything.values_list('date', flat=True).filter(trade_code=code))[::-1],
                'high': list(everything.values_list('high', flat=True).filter(trade_code=code))[::-1],
                'low': list(everything.values_list('low', flat=True).filter(trade_code=code))[::-1],
                'open': list(everything.values_list('open', flat=True).filter(trade_code=code))[::-1],
                'close': list(everything.values_list('close', flat=True).filter(trade_code=code))[::-1],
                'volume': list(everything.values_list('volume', flat=True).filter(trade_code=code))[::-1],
            }
        masterDict = json.dumps(masterDict)
        
        context = {
            'obj': page_obj,
            # 'dates': uniqueDate,
            # 'highs': highs,
            # 'lows': lows,
            # 'opens': opens,
            # 'closes': closes,
            # 'volumes': volumes,

            'alltradecode': allTradecode,
            'masterdict':masterDict,


        }
        



        return render(request, self.template_name, context=context)

class EditData(View):
    template_name = 'visualization/edit.html'
    def get(self, request, *args, **kwargs):
        id = self.kwargs['id']
        instance = ReadCSV.objects.get(pk = id)
        form = EditReadCSVForm(instance=instance)
        context = {
            'form': form,
            'id': id,
        }
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        id = self.kwargs['id']
        path = self.request.META.get('HTTP_REFERER')
        print(path)
        instance = ReadCSV.objects.get(pk = id)
        form = EditReadCSVForm(request.POST)

        if form.is_valid:
            form = EditReadCSVForm(request.POST, instance=instance)
            form.save()
            return redirect('/')
        else:
            pass
        return render(request, self.template_name, {'form': form})