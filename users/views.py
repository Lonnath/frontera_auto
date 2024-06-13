# DJANGO IMPORTS 
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# REST_FRAMEWORK IMPORTS
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# UTILS IMPORTS
import json
from users.models import Usuario
from users.utils import generate_token
from django.contrib.auth.hashers import make_password, check_password

@csrf_exempt
@require_http_methods(["POST"])
def login(request):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')

    try:
        user = Usuario.objects.get(usuario=username)
        
        if check_password(password, user.password):
            token = generate_token(user)
            return JsonResponse(
                {
                    'response': 'Usuario logueado correctamente',
                    'token': token,
                    'username': user.usuario,
                }, status=200)
        
        else:
            return JsonResponse({'response': 'Usuario o contraseña incorrectos'}, status=400)
    except Usuario.DoesNotExist:
        return JsonResponse({'response': 'Usuario no existe.'}, status=400)
    except Exception as e:
        return JsonResponse({'response': str(e)}, status=400)

