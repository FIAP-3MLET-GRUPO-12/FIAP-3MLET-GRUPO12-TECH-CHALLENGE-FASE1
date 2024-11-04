
from typing import Dict, List
from app.schemas.product_report_schema import ProductReportSchema


class ProductReportGenerator:
    def __init__(self, product: List[Dict[str, str | int]], year: int, type: str) -> None: 
        self.product = product
        self.year = year
        self.type = type

    def generate(self):
        report: ProductReportSchema = {
            "type": self.type,
            "year": self.year,
            "categories": []
        }
        
        categories = [item for item in self.product if item['category'] == item['name']]
        
        for category in categories:
            category_item = {
                "name": category['category'],
                "value": category['value'],
                "subcategories": []
            }
            
            subcategories = [item for item in self.product if item['category'] != item['name']]
            
            for subcategory in subcategories:
                if subcategory['category'] == category['category']:
                    subcategory_item = {
                        "name": subcategory['name'],
                        "value": subcategory['value']
                    }
                    category_item["subcategories"].append(subcategory_item)
            
            report["categories"].append(category_item)
        return report