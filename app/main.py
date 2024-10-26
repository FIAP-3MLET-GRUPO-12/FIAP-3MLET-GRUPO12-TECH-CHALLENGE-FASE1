from fastapi import FastAPI
from app.config import settings
from app.db.database import init_db
from app.routers import user_router
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield
    
app = FastAPI(lifespan=lifespan)

app.include_router(user_router.router, prefix="/users", tags=["users"])
