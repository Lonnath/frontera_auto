# DJANGO IMPORTS 

from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# UTILS IMPORTS

import json
import jwt
from users.decorators import jwt_token_required
from frontera_auto_back.settings import SECRET_KEY

# SERIALIZERS

from .serializers import *

# OBJECTS IMPORTS

from users.models import Usuario
from .models import *

# PESO LOGIC 

@csrf_exempt
@require_http_methods(["POST"])
@jwt_token_required
def create_peso(request) :
    auth_header = request.headers.get('Authorization')
    token = auth_header.split(' ')[1]
    payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    data = json.loads(request.body)
    data['usuario'] = payload['id']
    serializer = PesajeSubproductoSerializer(data=data)

    if serializer.is_valid():
        pesaje_subproducto_serializer = serializer.save()
        return JsonResponse({'response': f'Peso creado correctamente para la Viscera { pesaje_subproducto_serializer.id }'}, status=200)
    else:
        return JsonResponse({'response': f'ERROR: No se pudo guardar el registro, Causa: {serializer.errors}.'}, status=400)

@csrf_exempt
@require_http_methods(["GET"])
@jwt_token_required
def get_peso(request, id=int):
    
    peso_data = None

    try:
        peso_data = PesajeSubproducto.objects.get(id=id)
    except PesajeSubproducto.DoesNotExist:
        return JsonResponse({'response': 'Pesaje Subproducto no encontrado'}, status=400)

    serializer = PesajeSubproductoSerializer(peso_data)
    out_data = {}
    out_data['pesaje_subproducto'] = serializer.data
    out_data['viscera'] = {
        'turno': peso_data.vicera.turno,
        'cifra': peso_data.vicera.cifra,
        'peso': peso_data.vicera.peso,
        'serie': peso_data.vicera.serie,
        'responsable_firma': peso_data.vicera.responsable_firma,
        'tipo_vicera': peso_data.vicera.tipo_vicera,

    }
    return JsonResponse({'response': 'Pesaje Subproducto consultada correctamente', 'Message': out_data}, status=200)


@csrf_exempt
@require_http_methods(["GET"])
@jwt_token_required
def get_pesos_all(request):

    peso_data = None

    try:
        peso_data = PesajeSubproducto.objects.all()
    except PesajeSubproducto.DoesNotExist:
        return JsonResponse({'response': 'Pesaje Subproducto no encontrado'}, status=400)

    serializer = PesajeSubproductoSerializer(peso_data, many=True)
    
    return JsonResponse({'response': 'Pesaje Subproducto consultada correctamente', 'Message': serializer.data}, status=200)



# VISCERAS LOGIC

@csrf_exempt
@require_http_methods(["POST"])
@jwt_token_required
def create_viscera(request) :

    data = json.loads(request.body)
    serializer = ViceraSerializer(data=data)
    if serializer.is_valid():
        viscera_data = serializer.save()
        return JsonResponse({'response': 'Viscera creada correctamente', 'Message': {'id': viscera_data.id }}, status=200)
    else:
        return JsonResponse({'response': f'ERROR: No se pudo guardar el registro, Causa: {serializer.errors}.'}, status=400)



@csrf_exempt
@require_http_methods(["GET"])
@jwt_token_required
def get_viscera(request, id=int):

    visceras_data = None

    try:
        visceras_data = Vicera.objects.get(id=id)
    except Vicera.DoesNotExist:
        return JsonResponse({'response': 'Viscera no encontrada'}, status=400)

    serializer = ViceraSerializer(visceras_data)

    return JsonResponse({'response': 'Viscera consultada correctamente', 'Message': {'data': serializer.data}}, status=200)


@csrf_exempt
@require_http_methods(["GET"])
@jwt_token_required
def get_visceras_all(request):

    visceras_data = None
    try:
        visceras_data = Vicera.objects.all()
    except Vicera.DoesNotExist:
        return JsonResponse({'response': 'Visceras consultadas incorrectamente'}, status=400)

    serializer = ViceraSerializer(visceras_data, many=True)
    return JsonResponse({'response': 'Visceras consultadas correctamente', 'Message': {'data': serializer.data}}, status=200)