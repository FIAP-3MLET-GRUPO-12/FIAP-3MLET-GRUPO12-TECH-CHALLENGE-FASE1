from fastapi import APIRouter, HTTPException
from app.models.user_model import User
from app.schemas.user_schema import UserSchema

router = APIRouter()

@router.post("/", response_model=UserSchema)
async def create_user(user: UserSchema):
    new_user = User(name=user.name, age=user.age)
    await new_user.insert()
    return new_user