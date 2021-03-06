from datetime import date
from queue import Empty
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from django.views import View

from load_data.models import ReadCSV

import json

from visualization.forms import EditReadCSVForm
# Create your views here.

class TableView(View):
    template_name = 'visualization/index.html'
    
    def get(self, request, *args, **kwargs):
        everything = ReadCSV.objects.all()

        p = Paginator(everything, 27)
        page_number = request.GET.get('page')
        try:
            page_obj = p.get_page(page_number)
        except PageNotAnInteger:
            page_obj = p.page(1)
        except EmptyPage:
            page_obj = p.page(p.num_pages)

        allTradecode = list(dict.fromkeys(list(everything.values_list('trade_code', flat=True))))
        page_trade_code = allTradecode[int(page_number or 1)-1]

        f = open('stock_market_data.json')
        data = json.load(f)
        data = json.dumps(data)
        
        context = {
            'obj': page_obj,
            'alltradecode': allTradecode,
            'page_trade_code': page_trade_code
        }
        print(page_trade_code)

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

class GetJson(View):
    def get(self, request, *args, **kwargs ):
        trade_code = self.kwargs['trade_code']
        chart_obj = ReadCSV.objects.filter(trade_code = trade_code).order_by('date')
        chart_data = {
            'trade_code': trade_code,
            'date': [obj.date for obj in chart_obj],
            'high': [obj.high for obj in chart_obj],
            'low': [obj.low for obj in chart_obj],
            'open': [obj.open for obj in chart_obj],
            'close': [obj.close for obj in chart_obj],
            'volume': [obj.volume for obj in chart_obj],
        }
        return JsonResponse(chart_data)