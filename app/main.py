import logging
from fastapi import FastAPI

from app.db.database import init_db

from app.routers import user_router, product_router

from contextlib import asynccontextmanager

from app.utils.trade_setup import trade_setup
from app.utils.product_setup import product_setup

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    await startup()
    yield
    
app = FastAPI(lifespan=lifespan)

app.include_router(user_router.router, prefix="/users", tags=["users"])
app.include_router(product_router.router, prefix="/products", tags=["products"])

logging.basicConfig(level=logging.INFO)

async def startup(): 
   await product_setup()
   await trade_setup()
