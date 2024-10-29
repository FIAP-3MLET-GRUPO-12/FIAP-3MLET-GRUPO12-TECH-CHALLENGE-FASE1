import pandas as pd
from typing import List
from typing import Dict
from typing import Any
from datetime import datetime

from app.utils.product_type_enum import ProductType

def parse_data_frame_to_product_json(df: pd.DataFrame, type: ProductType) -> List[Dict[str, Any]]:
    """
    Converts a pandas DataFrame into a list of JSON dictionaries, where each dictionary represents a product.

    Args:
        df (pd.DataFrame): DataFrame containing product data.
        type (ProductType): Product type, based on the ProductType enum.

    Returns:
        List[Dict[str, Any]]: List of JSON dictionaries, where each dictionary contains product information and annual values.

    Structure of the returned dictionary:
        {
            "id": <value of the 'id' field in the row>,
            "name": <value of the 'product' field in the row>,
            "category": <value of the 'control' field in the row>,
            "type": <name of the product type>,
            "years": [
                {
                    "year": <year>,
                    "value": <value of the field corresponding to the year>
                },
                ...
            ]
        }
    """
    data_json = []
    for _, row in df.iterrows():
        data = {
            "id": row["id"],
            "name": row["produto"],
            "category": row["control"],
            "type": type.value,
            "years": []
        }

        current_year = datetime.now().year

        for year in range(1970, current_year + 1):
            year_str = str(year)
            if year_str in row:
                data["years"].append({
                    "year": int(year_str),
                    "value": row[year_str]
                })    

        data_json.append(data)

    return data_json