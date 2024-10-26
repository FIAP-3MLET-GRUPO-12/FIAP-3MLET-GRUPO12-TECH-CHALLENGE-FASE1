from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.models.user_model import User
from app.config import settings

async def init_db():
    client = AsyncIOMotorClient(f"{settings.MONGODB_URL}/{settings.MONGODB_DB}")
    await init_beanie(database=client[settings.MONGODB_DB], document_models=[User])