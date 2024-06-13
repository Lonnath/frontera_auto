from datetime import datetime, timedelta
from frontera_auto_back.settings import SECRET_KEY
import jwt
from pytz import timezone

def generate_token(user):
    timezone_deseado = timezone('America/Bogota')
    now = datetime.now(timezone_deseado)
    expiration = now + timedelta(days=1)
    expiration = expiration.astimezone(timezone_deseado)
    token = jwt.encode({'username': user.usuario, 'id': user.id, 'exp': expiration},
                       SECRET_KEY, algorithm='HS256')
    return token