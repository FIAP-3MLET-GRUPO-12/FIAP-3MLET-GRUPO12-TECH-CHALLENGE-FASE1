import logging
from app.config import settings
from app.models.product_model import Product
from app.utils.csv_downloader import download_csv_from_url
from app.utils.json_utils import parse_data_frame_to_product_json
from app.utils.product_type_enum import ProductType

async def product_setup():
   if await products_exist():
       return
   
   base_url = settings.BASE_URL_CSV_VITIBRASIL
   csv_files = [
        ("/Producao.csv", ProductType.PRODUCTION, ';'),
        ("/ProcessaViniferas.csv", ProductType.PROCESSING_VINES, ';'),
        ("/ProcessaAmericanas.csv", ProductType.PROCESSING_AMERICAN, '\t'),
        ("/ProcessaMesa.csv", ProductType.PROCESSING_TABLE_GRAPES , '\t'),
        ("/ProcessaSemclass.csv", ProductType.PROCESSING_UNRATED, '\t'),
        ("/Comercio.csv", ProductType.COMMERCIALIZATION, ';')
   ]
   
   products = []
   logging.info(" - Downloading product data...")
   for file_suffix, product_type, delimiter in csv_files:
        logging.info(f" - Downloading {file_suffix}...")
        df = download_csv_from_url(base_url + file_suffix, delimiter)
        json_data = parse_data_frame_to_product_json(df, product_type)
        products.extend([Product(**product) for product in json_data])

   labeled_products = label_all_products(products)
   logging.info(" - Inserting product data...")
   await insert_all_products(labeled_products)  
   logging.info(" - Product data inserted successfully!")

async def products_exist() -> bool:
    existing_products = await Product.find_all().to_list()
    return bool(existing_products)

async def insert_all_products(products: list[Product]):
    await Product.insert_many(products)

def label_all_products(products: list[Product]) -> list[Product]:
    return label_product_data_category(products)

def label_product_data_category(products: list[Product]) -> list[Product]:
    """
    Labels the product data category for a list of products.

    This function iterates over a list of Product objects and assigns a category to each product.
    If a product's category is in uppercase, it sets the current category to that product's category.
    If a product's category is not in uppercase, it assigns the current category to that product's category.

    Args:
        products (list[Product]): A list of Product objects.

    Returns:
        list[Product]: The list of Product objects with updated categories.
    """
    category = ""

    for product in products:
        if product.category.isupper():
            category = product.category
        else:
            product.category = category

    return products