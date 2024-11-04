from fastapi import APIRouter, HTTPException
from app.models.product_model import Product
from app.schemas.product_report_schema import ProductReportSchema
from app.schemas.product_schema import ProductSchema

from app.utils.product_report_generator import ProductReportGenerator
from app.utils.product_type_enum import ProductType

router = APIRouter()

# @router.get("/", response_model=ProductReportSchema)
@router.get("/")
async def get_all_production():
  report = await Product.find_by_type_with_year(ProductType.PRODUCTION.value, specific_year=2023)
  if not report:
    raise HTTPException(status_code=404, detail="No production products found")


  
  return report