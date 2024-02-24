from django.urls import path, include
from . import views

urlpatterns = [
    path('upload_invoice/', views.upload_invoice, name='upload_invoice'),
]
