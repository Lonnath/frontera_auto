from django.urls import path
from .views import *

urlpatterns = [

    # PESO ENDPOINTS
    path('peso/create/', create_peso, name='peso/create'),
    path('peso/get_peso/<int:id>/', get_peso, name='peso/get_peso'),
    path('peso/get_pesos_all/', get_pesos_all, name='peso/get_pesos'),

    # VISCERAS ENDPOINTS
    path('visceras/create/', create_viscera, name='viscera/create'),
    path('visceras/get_viscera/<int:id>/',
         get_viscera, name='viscera/get_viscera'),
    path('visceras/get_visceras_all/',
         get_visceras_all, name='viscera/get_visceras'),
    
    # DECOMISO ENDPOINTS
    path('decomiso/create/', create_decomiso, name='decomiso/create'),
    path('decomiso/get_decomiso/<int:id>/',
         get_decomiso, name='decomiso/get_decomiso'),
    path('decomiso/get_decomisos_all/', get_decomisos_all, name='decomiso/get_decomisos'),
    path('decomiso/get_pdf_decomiso/<int:id>/', get_pdf_decomiso, name='decomiso/get_pdf_decomiso'),
]
