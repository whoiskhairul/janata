from django.urls import path

from visualization.views import TableView, EditData, GetJson

urlpatterns = [
    path('', TableView.as_view(), name='visual'),
    path('edit/<int:id>', EditData.as_view(), name='editform'),
    path('getjson/<str:trade_code>', GetJson.as_view(), name='getjson'),
]
