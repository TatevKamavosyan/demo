# textprocessor/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.text_processor_view, name='text_processor'),
    path('text/<int:pk>/', views.text_detail_view, name='text_detail'),
]
