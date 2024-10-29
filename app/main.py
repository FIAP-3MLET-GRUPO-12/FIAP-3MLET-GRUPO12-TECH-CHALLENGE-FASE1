from fastapi import FastAPI

from app.db.database import init_db

from app.routers import user_router
from contextlib import asynccontextmanager

from app.utils.product_setup import product_setup

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    await startup()
    yield
    
app = FastAPI(lifespan=lifespan)

app.include_router(user_router.router, prefix="/users", tags=["users"])

async def startup(): 
   await product_setup()
