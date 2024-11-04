from beanie import Document
from passlib.context import CryptContext
from pydantic import EmailStr


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(Document):
  email: EmailStr
  hashed_password: str

  def verify_password(self, password: str) -> bool:
    return pwd_context.verify(password, self.hashed_password) 
  
  @classmethod
  def hash_password(cls, password: str) -> str:
    return pwd_context.hash(password)
  
  class Settings:
    collection = "users"