from django.contrib import admin
from load_data.models import ReadCSV
# Register your models here.

class ReadCSVAdmin(admin.ModelAdmin):
    list_display = ('date', 'trade_code', 'high', 'low', 'volume')

admin.site.register(ReadCSV, ReadCSVAdmin)