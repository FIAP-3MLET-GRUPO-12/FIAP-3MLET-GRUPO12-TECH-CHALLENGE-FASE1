from typing import Dict, List
from app.schemas.product_report_schema import ProductReportSchema

class ProductReportGenerator:
    def __init__(self, product: List[Dict[str, str | int]], year: int, type: str) -> None: 
        # Inicializa a classe com a lista de produtos, ano e tipo de relatório
        self.product = product
        self.year = year
        self.type = type

    def generate(self):
        # Cria a estrutura inicial do relatório
        report: ProductReportSchema = {
            "type": self.type,
            "year": self.year,
            "categories": []
        }
        
        # Filtra as categorias principais (onde 'category' é igual a 'name')
        categories = [item for item in self.product if item['category'] == item['name']]
        
        for category in categories:
            # Cria um item de categoria com nome, valor e subcategorias vazias
            category_item = {
                "name": category['category'],
                "value": category['value'],
                "subcategories": []
            }
            
            # Filtra as subcategorias (onde 'category' é diferente de 'name')
            subcategories = [item for item in self.product if item['category'] != item['name']]
            
            for subcategory in subcategories:
                # Adiciona subcategorias ao item de categoria correspondente
                if subcategory['category'] == category['category']:
                    subcategory_item = {
                        "name": subcategory['name'],
                        "value": subcategory['value']
                    }
                    category_item["subcategories"].append(subcategory_item)
            
            # Adiciona o item de categoria ao relatório
            report["categories"].append(category_item)
        
        # Retorna o relatório gerado
        return report