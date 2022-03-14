from django.urls import path

from visualization.views import TableView

urlpatterns = [
    path('', TableView.as_view())
]
