from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.models.user_model import User
from app.config import settings

async def init_db():
    mongo_url = f"{settings.MONGODB_URL}"
    client = AsyncIOMotorClient(mongo_url)
    try:
        await init_beanie(database=client[settings.MONGODB_DB], document_models=[User])
    except Exception as e:
        print(f"MONGO_DB_INIT: {e}")
        client.close()
    
        