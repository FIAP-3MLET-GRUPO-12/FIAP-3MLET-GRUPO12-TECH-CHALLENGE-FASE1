from pydantic import BaseSettings

class Settings(BaseSettings):
  MONGODB_URL: str
  MONGODB_DB: str
  
  class Config:
    env_file = ".env"
    env_file_encoding = "utf-8"
    
settings = Settings()