from pydantic_settings import BaseSettings

class Settings(BaseSettings):
  MONGODB_URL: str
  MONGODB_DB: str
  BASE_URL_CSV_VITIBRASIL: str
  SECRET_KEY: str
  ALGORITHM: str
  ACCESS_TOKEN_EXPIRE_MINUTES: int
  
  class Config:
    env_file = ".env"
    env_file_encoding = "utf-8"
    
settings = Settings()