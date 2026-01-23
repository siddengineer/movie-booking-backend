from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
def get_current_user(token: str = Depends(oauth2_scheme)):
    if token != "fake-token":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
        )
    return {"username": "testuser"}



