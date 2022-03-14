from ast import Return
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

import csv
import pandas as pd

from load_data.forms import UploadFileForm
from load_data.models import ReadCSV
# Create your views here.
class UploadView(View):

    template_name = 'load_data/upload.html'

    def get(self, request, *args, **kwargs):
        form = UploadFileForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):

        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            form = UploadFileForm()
            reader = request.FILES['file']
            df = pd.read_csv(reader)
            print(df)
            for ind in df.index:
                date = df['date'][ind]
                trade_code = df['trade_code'][ind]
                high = float(df['high'][ind].replace(',',''))
                low = float(df['low'][ind].replace(',',''))
                open = float(df['open'][ind].replace(',',''))
                close = float(df['close'][ind].replace(',',''))
                volume = float(df['volume'][ind].replace(',',''))

                ReadCSV.objects.create(date = date, trade_code=trade_code, high=high, low=low, open=open, close=close, volume=volume)
            
        else:
            pass
                

                

            
        return render(request, self.template_name, {'form': form})
        