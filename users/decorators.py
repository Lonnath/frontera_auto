from django.conf import settings
from django.http import JsonResponse
from django.core.cache import cache
from jwt.exceptions import ExpiredSignatureError
from .models import Usuario
from datetime import datetime
from pytz import timezone
import jwt

def jwt_token_required(view_func):
    def _wrapped_view(request, *args, **kwargs): 
        auth_header = request.headers.get('Authorization')
        if auth_header:
            token = auth_header.split(' ')[1]
            try:
                payload = jwt.decode(
                    token, settings.SECRET_KEY, algorithms=['HS256'])

                if (cache.get(payload['id'])):
                    token_modificado = cache.get(payload['id'])
                    expiration_time = token_modificado['exp']
                    timezone_deseado = timezone('America/Bogota')
                    now = datetime.now(timezone_deseado)

                    if expiration_time and now > expiration_time:
                        return JsonResponse({'error': 'Token ha caducado'}, status=401)

                expiration_time = payload.get('exp')
                if expiration_time is None:
                    return JsonResponse({'error': 'Token no valido'}, status=401)
                
                expiration_time_date = datetime.fromtimestamp(expiration_time, timezone('America/Bogota'))
                timezone_deseado = timezone('America/Bogota')
                now = datetime.now(timezone_deseado)
                
                if expiration_time_date and now > expiration_time_date:
                    return JsonResponse({'error': 'Token ha caducado'}, status=401)
                
                user = Usuario.objects.filter(id=payload['id']).first()

                request.user = user
                if user:
                    return view_func(request, *args, **kwargs)
                else:
                    return JsonResponse({'error': 'Usuario no válido'}, status=401)

            except jwt.exceptions.DecodeError:
                return JsonResponse({'error': 'Token invalido'}, status=401)
            except ExpiredSignatureError:
                return JsonResponse({'error': 'Token ha caducado'}, status=401)
            except Usuario.DoesNotExist:
                return JsonResponse({'error': 'Usuario no encontrado'}, status=401)
        else:
            return JsonResponse({'error': 'Token no proporcionado'}, status=401)
    return _wrapped_view