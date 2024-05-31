from django.urls import path
from . import views

urlpatterns = [
    path('ordinary_coders/', views.ordinary_coders, name='ordinary_coders'),
    path('geeks_for_geeks/', views.geeks_for_geeks, name='geeks_for_geeks'),
]