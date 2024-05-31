from django.urls import path
from . import views

urlpatterns = [
    path('great_dev_medium/', views.great_dev_medium, name='great_dev_medium'),
]