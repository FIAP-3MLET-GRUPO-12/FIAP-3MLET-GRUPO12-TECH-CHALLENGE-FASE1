from fastapi import APIRouter, HTTPException, status
from app.auth.auth import create_access_token
from app.models.user_model import User
from app.schemas.token_schema import TokenSchema
from app.schemas.user_schema import UserSchema

router = APIRouter()

@router.post("/", response_model=UserSchema)
async def create_user(user: UserSchema):
    user_in_db = await User.find_one({"email": user.email})
    if user_in_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )

    new_user = User(email=user.email, hashed_password=User.hash_password(user.password))
    await new_user.insert()
    return {"msg": "User created successfully"}

@router.post("/login", response_model=TokenSchema)
async def login(user: UserSchema):
    db_user = await User.find_one({"email": user.email})
    if db_user is None or not db_user.verify_password(user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Wrong Credentials", 
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": db_user.email})
    return {"access_token": access_token, "token_type": "bearer"}

