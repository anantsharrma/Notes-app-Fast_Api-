import os

from jose import jwt
from datetime import datetime, timedelta, timezone
from pwdlib import PasswordHash
from dotenv import load_dotenv
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
EXPIRES_IN = 30
password_hash = PasswordHash.recommended()
def hash_password(password: str) -> str :
        return password_hash.hash(password)
def verify_password(
        plain_password, hashed_password
) -> bool:
    return password_hash.verify(
        plain_password, hashed_password
    )
def get_access_token(data: dict):
    Data = data.copy()
    Data["exp"] = datetime.now(timezone.utc) + timedelta(minutes=EXPIRES_IN)
    token = jwt.encode(Data, SECRET_KEY, algorithm=ALGORITHM)
    return token

