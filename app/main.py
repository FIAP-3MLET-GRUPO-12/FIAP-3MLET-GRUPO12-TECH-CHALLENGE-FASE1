import logging
from fastapi import FastAPI

from app.db.database import init_db

from app.routers import production_router,processing_router

from contextlib import asynccontextmanager

from app.utils.trade_setup import trade_setup
from app.utils.product_setup import product_setup

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    await startup()
    yield
    
app = FastAPI(lifespan=lifespan)

app.include_router(production_router.router, prefix="/production", tags=["production"])
app.include_router(processing_router.router, prefix="/processing", tags=["processing"])

logging.basicConfig(level=logging.INFO)

async def startup(): 
   await product_setup()
   await trade_setup()
