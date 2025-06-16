from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserRead, Token
from app.crud.user   import create_user, authenticate_user, get_user_by_email
from app.db.session  import get_session
from app.core.security import create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UserRead)
def register(user_in: UserCreate, db: Session = Depends(get_session)):
    if get_user_by_email(db, user_in.email):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Email already registered")
    return create_user(db, user_in)


@router.post("/login", response_model=Token)
def login(
    form: OAuth2PasswordRequestForm = Depends(),
    db:   Session                   = Depends(get_session),
):
    user = authenticate_user(db, form.username, form.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid credentials")

    return {
        "access_token": create_access_token({"sub": user.email}),
        "token_type":   "bearer",
    }
