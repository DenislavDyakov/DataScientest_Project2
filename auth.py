import jwt
from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from passlib.context import CryptContext
from datetime import datetime, timedelta


class AuthenticationHandler:
    security = HTTPBearer()
    password = CryptContext(schemes=["sha256_crypt"])
    secret = 'SECRET'

    def get_hashed_password(self, password):
        return self.password.hash(password)

    def verify_password(self, password, hashed_password):
        return self.password.verify(password, hashed_password)

    def create_token(self, user_id):
        payload = {
            'exp': datetime.utcnow() + timedelta(hours=1),
            'iat': datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(payload, self.secret, algorithm='HS256')

    def decode_token(self, token):
        try:
            payload = jwt.decode(token, self.secret, algorithms=['HS256'])
            return payload['sub']
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail='Token has expired. Please, log in again.')
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail='Invalid token.')

    def auth_wrapper(self, auth: HTTPAuthorizationCredentials = Security(security)):
        return self.decode_token(auth.credentials)







