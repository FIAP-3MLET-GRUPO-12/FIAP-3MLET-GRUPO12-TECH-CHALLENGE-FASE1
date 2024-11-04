from pydantic import BaseModel

"""
Modela a estrutura do relatório referente à categoria de Processamento
"""
class ProductReportSchema(BaseModel):
    type: str
    name: str
    year: int
    categories: list["CategoryItem"]
    
"""
Indica a estrutura de um item de categoria
"""
class CategoryItem(BaseModel):
    name: str
    value: int
    subcategories: list["SubItem"]
    
"""
Indica a estrutura de um subitem de categoria
"""
class SubItem(BaseModel):
    name: str
    value: int

