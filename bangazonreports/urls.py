from django.urls import path
from .views import expensive_list
from .views import inexpensive_list

urlpatterns = [
    path('reports/expensive', expensive_list),
    path('reports/inexpensive', inexpensive_list),
]