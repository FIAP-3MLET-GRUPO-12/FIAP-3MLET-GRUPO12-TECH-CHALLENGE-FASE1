from typing import Dict, List
from app.schemas.product_report_schema import ProductReportSchema
from app.schemas.trade_report_schema import TradeReportSchema

class ReportGenerator:
    """
    Classe para gerar relatórios de produtos e negociações.

    Atributos:
        year (int): Ano do relatório.
    """

    def __init__(self, year: int) -> None:
        """
        Inicializa a classe com o ano do relatório.

        Args:
            year (int): Ano do relatório.
        """
        self.year = year
        
    def create_trade_report(self, trades: List[Dict[str, str | int]], derivative, type) -> TradeReportSchema:
        """
        Cria um relatório de negociações.

        Args:
            trades (List[Dict[str, str | int]]): Lista de negociações.
            derivative: Derivativo das negociações.
            type: import ou export.

        Returns:
            TradeReportSchema: Estrutura do relatório de negociações.
        """
        # Cria a estrutura inicial do relatório
        report: TradeReportSchema = {
            "type": type,
            "year": self.year,
            "derivative": derivative,
            "trades": []
        }
        
        for trade in trades:
            # Cria um item de negociação com país, categoria e valor
            trade_item = {
                "country": trade['country'],
                "quantity": trade['year_value'].qtd,
                "value": trade['year_value'].value
            }
            
            # Adiciona o item de negociação ao relatório
            report["trades"].append(trade_item)
        
        # Retorna o relatório gerado
        return report
        

    def create_product_report(self, product: List[Dict[str, str | int]], type_value: str) -> ProductReportSchema:
        """
        Cria um relatório de produtos.

        Args:
            product (List[Dict[str, str | int]]): Lista de produtos.
            type_value (str): Tipo de relatório.

        Returns:
            ProductReportSchema: Estrutura do relatório de produtos.
        """
        # Cria a estrutura inicial do relatório
        report: ProductReportSchema = {
            "type": type_value,
            "year": self.year,
            "categories": []
        }
        
        # Filtra as categorias principais (onde 'category' é igual a 'name')
        categories = [item for item in product if item['category'] == item['name']]
        
        for category in categories:
            # Cria um item de categoria com nome, valor e subcategorias vazias
            category_item = {
                "name": category['category'],
                "value": category['value'],
                "subcategories": []
            }
            
            # Filtra as subcategorias (onde 'category' é diferente de 'name')
            subcategories = [item for item in product if item['category'] != item['name']]
            
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