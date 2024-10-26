from beanie import Document

class User(Document):
  name: str
  age: int
  
  class Settings:
    collection = "users"