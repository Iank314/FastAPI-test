from __future__ import annotations

from uuid import UUID

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy.orm import Session

from app.db.session  import get_session
from app.crud.user   import get_user_by_email
from app.core.security import decode_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_db(session: Session = Depends(get_session)):
    return session


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db:    Session = Depends(get_db),
):
    try:
        token_data = decode_access_token(token)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    user = get_user_by_email(db, token_data.email)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return user
