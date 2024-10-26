from fastapi import FastAPI
from app.config import settings
from app.db.database import init_db
from app.routers import user_router

async def lifespan(app: FastAPI) -> None:
    await init_db()
    
app = FastAPI(lifespan=lifespan)

app.include_router(user_router.router, prefix="/users", tags=["users"])
