from typing import Dict, List
from app.schemas.product_report_schema import ProductReportSchema
from app.schemas.trade_report_schema import TradeReportSchema

class ReportGenerator:
    """
    Class to generate product and trade reports.

    Attributes:
        year (int): Report year.
    """

    def __init__(self, year: int) -> None:
        """
        Initializes the class with the report year.

        Args:
            year (int): Report year.
        """
        self.year = year
        
    def create_trade_report(self, trades: List[Dict[str, str | int]], derivative, type) -> TradeReportSchema:
        """
        Creates a trade report.

        Args:
            trades (List[Dict[str, str | int]]): List of trades.
            derivative: Derivative of the trades.
            type: import or export.

        Returns:
            TradeReportSchema: Structure of the trade report.
        """
        # Creates the initial structure of the report
        report: TradeReportSchema = {
            "type": type,
            "year": self.year,
            "derivative": derivative,
            "trades": []
        }
        
        for trade in trades:
            # Creates a trade item with country, category, and value
            trade_item = {
                "country": trade['country'],
                "quantity": trade['year_value'].qtd,
                "value": trade['year_value'].value
            }
            
            # Adds the trade item to the report
            report["trades"].append(trade_item)
        
        # Returns the generated report
        return report
        

    def create_product_report(self, product: List[Dict[str, str | int]], type_value: str) -> ProductReportSchema:
        """
        Creates a product report.

        Args:
            product (List[Dict[str, str | int]]): List of products.
            type_value (str): Report type.

        Returns:
            ProductReportSchema: Structure of the product report.
        """
        # Creates the initial structure of the report
        report: ProductReportSchema = {
            "type": type_value,
            "year": self.year,
            "categories": []
        }
        
        # Filters the main categories (where 'category' is equal to 'name')
        categories = [item for item in product if item['category'] == item['name']]
        
        for category in categories:
            # Creates a category item with name, value, and empty subcategories
            category_item = {
                "name": category['category'],
                "value": category['value'],
                "subcategories": []
            }
            
            # Filters the subcategories (where 'category' is different from 'name')
            subcategories = [item for item in product if item['category'] != item['name']]
            
            for subcategory in subcategories:
                # Adds subcategories to the corresponding category item
                if subcategory['category'] == category['category']:
                    subcategory_item = {
                        "name": subcategory['name'],
                        "value": subcategory['value']
                    }
                    category_item["subcategories"].append(subcategory_item)
            
            # Adds the category item to the report
            report["categories"].append(category_item)
        
        # Returns the generated report
        return report