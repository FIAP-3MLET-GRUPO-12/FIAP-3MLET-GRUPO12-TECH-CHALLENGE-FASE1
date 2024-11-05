import bcrypt
from beanie import Document
from pydantic import EmailStr

class User(Document):
  email: EmailStr
  hashed_password: str

  def verify_password(self, password: str) -> bool:
    """
    Verifies if the provided password matches the stored hashed password.

    Args:
        password (str): The plain text password to verify.

    Returns:
        bool: True if the password matches, False otherwise.
    """  
    return bcrypt.checkpw(password.encode('utf-8'), self.hashed_password.encode('utf-8')) 
  
  @classmethod
  def hash_password(cls, password: str) -> str:
    """
    Hashes the provided password and returns the hashed password.

    Args:
      password (str): The plain text password to hash.

    Returns:
      str: The hashed password.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
  
  class Settings:
    collection = "users"