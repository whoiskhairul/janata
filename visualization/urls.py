from django.urls import path

from visualization.views import TableView, EditData

urlpatterns = [
    path('', TableView.as_view(), name='visual'),
    path('edit/<int:id>', EditData.as_view(), name='editform'),
]
