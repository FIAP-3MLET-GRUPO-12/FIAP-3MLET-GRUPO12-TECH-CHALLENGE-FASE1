import math
from beanie import PydanticObjectId
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
        if not isinstance(row["control"], str):
            row["control"] = row.get("produto") or row.get("cultivar") or row.get("Produto")

        data = {
            "id": PydanticObjectId(),
            "name": row.get("produto") or row.get("cultivar") or row.get("Produto"),
            "category": row["control"],
            "type": type.value,
            "years": []
        }

        current_year = datetime.now().year

        for year in range(1970, current_year + 1):
            year_str = str(year)
           
            if year_str in row:
                value = 0
                if isinstance(row[year_str], str):
                   row[year_str] = remove_after_comma(row[year_str])
                   if row[year_str].isdigit():
                       value = int(row[year_str])   

                data["years"].append({
                    "year": int(year_str),
                    "value": value
                })    

        data_json.append(data)

    return data_json

def remove_after_comma(s):
    return s.split(',')[0]