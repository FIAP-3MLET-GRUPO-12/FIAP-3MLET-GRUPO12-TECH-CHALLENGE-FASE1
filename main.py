from fastapi import FastAPI
from beanie import init_beanie, Document
from motor.motor_asyncio import AsyncIOMotorClient
import asyncio

# Denifir um modelo Beanie
class User(Document):
    name: str
    age: int

    class Settings:
        collection = "users"
        
# Conectar ao MongoDB e inicializar o Beanie
async def init_db():
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    await init_beanie(database=client.my_database, document_models=[User])
        
async def lifespan():
    # Code before startup event
    await init_db()
    yield
    # Code after startup event
    
    
# Criar a aplicação FastAPI
app = FastAPI(lifespan=lifespan)

    
# Definir uma rota de exemplo
@app.post("/users")
async def create_user(user: User):
    await user.insert()
    return user.model_dump()
    
