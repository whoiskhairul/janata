from django.urls import path

from load_data.views import UploadView

urlpatterns = [
    path('upload/', UploadView.as_view()),
]
