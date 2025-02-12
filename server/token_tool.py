from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from jwt import PyJWTError
from ambiente import Ambiente
import jwt

class Token:
    SECRET_KEY = "UFG"
    ALGORITHM = "HS256"
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

    @staticmethod
    def criar(username_data: dict):
        to_encode = username_data.copy()
        return jwt.encode(to_encode, Token.SECRET_KEY, algorithm=Token.ALGORITHM)

    @staticmethod
    def verificar(token: str = Depends(oauth2_scheme)):
        try:
            payload = jwt.decode(token, Token.SECRET_KEY, algorithms=[Token.ALGORITHM])
            username: str = payload.get("sub")
            if username is None or username != Ambiente.usuario.nome:
                raise HTTPException(status_code=401, detail="Token inválido!")
            return username
        except PyJWTError:
            raise HTTPException(status_code=401, detail="Token inválido!")
