from sqlalchemy.orm import Session
from fastapi import Depends,APIRouter,HTTPException
from app import crud,schemas
from app.database import get_db
from app.auth.token import create_access_token
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/signup")
def signup(user:schemas.user_schema.UserCreate,db:Session=Depends(get_db)):
    new_user=crud.user_crud.create_user(user,db)
    return new_user

@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = schemas.user_schema.UserLogin(
        email=form_data.username,
        password=form_data.password
    )
    authenticated_user = crud.user_crud.authenticate_user(user, db)
    if not authenticated_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )
    access_token = create_access_token(
        {"user_id": authenticated_user.id}
    )
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }