from itertools import count
from django.shortcuts import render

from django.views import View

from load_data.models import ReadCSV

import json
# Create your views here.

class TableView(View):
    template_name = 'visualization/index.html'
    
    def get(self, request, *args, **kwargs):

        obj = ReadCSV.objects.filter(trade_code = 'AAMRATECH')

        dates = []
        dateobj = obj.values_list('date', flat=True)
        for d in dateobj:
            dates.append(str(d))
        alldates = json.dumps(dates.reverse())

        uniqueDate = list(dict.fromkeys(dates))
        uniqueDate = json.dumps(uniqueDate)

        highs = []
        highobj = obj.values_list('high', flat=True)
        for c in highobj:
            highs.append(float(c))
        highs = json.dumps(highs[::-1])

        lows = []
        lowobj = obj.values_list('low', flat=True)
        for c in lowobj:
            lows.append(float(c))
        lows = json.dumps(lows[::-1])

        opens = []
        openobj = obj.values_list('open', flat=True)
        for c in openobj:
            opens.append(float(c))
        opens = json.dumps(opens[::-1])

        closes = []
        closeobj = obj.values_list('close', flat=True)
        for c in closeobj:
            closes.append(float(c))
        closes = json.dumps(closes[::-1])

        volumes = []
        volumeobj = obj.values_list('volume', flat=True)
        for c in volumeobj:
            volumes.append(float(c))
        volumes = json.dumps(volumes[::-1])


        d = {
        'tradecode' : {
            'date' : ['2020-07-02', '2020-07-05', '2020-07-06', '2020-07-07', '2020-07-08', '2020-07-09', '2020-07-12', '2020-07-13', '2020-07-14', '2020-07-15',
                    '2020-07-16', '2020-07-19', '2020-07-20', '2020-07-21', '2020-07-22', '2020-07-23', '2020-07-26','2020-07-27', '2020-07-28', '2020-07-29',
                    '2020-07-30', '2020-08-03', '2020-08-04', '2020-08-05', '2020-08-06', '2020-08-09', '2020-08-10'],
            'high' : [23, 23, 23, 23, 23, 23.8, 23.9, 23.4, 23, 23, 23, 23, 23, 23.1, 23.6, 23.7, 23.9, 23.8, 24, 25.2, 25.9, 25.6, 25.6, 25, 26, 26.4, 26.2],
            'low': [23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23.2, 23.4, 23.5, 24.1, 24.5, 24.7, 24.5, 24.5, 24.9, 25.4, 25.5],
            'open': [23, 23, 23, 23, 23, 23, 23.2, 23.1, 23, 23, 23, 23, 23, 23, 23.5, 23, 23.5, 23.4, 23.7, 24.1, 25, 25.5, 25.3, 24.8, 24.9, 26.2, 26.2],
            'close': [23, 23, 23, 23, 23, 23.1, 23.1, 23.1, 23, 23, 23, 23, 23, 23, 23.1, 23.5, 23.4, 23.5, 23.9, 25, 25.4, 25.3, 24.8, 24.9, 25.8, 26.2, 25.6],
            'volume': [2005, 3400, 10500, 170, 3325, 44283, 22209, 77654, 2990, 4665, 7085, 6, 12726, 26121, 33754, 28574, 51325, 33870, 68336, 126507, 216512, 90096, 87772, 72482, 137456, 123713, 72269]
            }
        }
        d = json.dumps(d)

        everything = ReadCSV.objects.all()
        allTradecode = list(dict.fromkeys(list(ReadCSV.objects.values_list('trade_code', flat=True))))

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
            'obj': obj,
            'dates': uniqueDate,
            'highs': highs,
            'lows': lows,
            'opens': opens,
            'closes': closes,
            'volumes': volumes,

            'alltradecode': allTradecode,
            'masterdict':masterDict,

        }
        



        return render(request, self.template_name, context=context)
