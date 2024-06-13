from django.conf import settings
from django.contrib.auth.models import User
from django.http import JsonResponse
import jwt


class JWTAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        auth_header = request.headers.get('Authorization')
        if auth_header:
            token = auth_header.split(' ')[1]
            try:
                payload = jwt.decode(
                    token, settings.SECRET_KEY, algorithms=['HS256'])
                user = User.objects.get(username=payload['username'])
                # Agregar el usuario a la request para que esté disponible en las vistas
                request.user = user
            except jwt.exceptions.DecodeError:
                return JsonResponse({'error': 'Token inválido'}, status=401)
            except User.DoesNotExist:
                return JsonResponse({'error': 'Usuario no encontrado'}, status=401)

        response = self.get_response(request)

        return response
