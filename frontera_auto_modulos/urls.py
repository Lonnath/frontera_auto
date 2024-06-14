from django.urls import path
from .views import *

urlpatterns = [
    
    # PESO ENDPOINTS

    path('peso/create/', create_peso, name='peso/create'),
    path('peso/get_peso/<int:id>/', get_peso, name='peso/get_peso'),
    path('peso/get_pesos_all/', get_pesos_all, name='peso/get_pesos'),
    
    # VISCERAS ENDPOINTS
    path('visceras/create/', create_viscera, name='viscera/create'),
    path('visceras/get_viscera/<int:id>/', get_viscera, name='viscera/get_viscera'),
    path('visceras/get_visceras_all/', get_visceras_all, name='viscera/get_visceras'),
]
