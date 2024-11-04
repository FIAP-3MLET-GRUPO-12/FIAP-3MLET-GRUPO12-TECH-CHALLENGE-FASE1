from fastapi import APIRouter, HTTPException
from app.models.product_model import Product
from app.schemas.product_report_schema import ProductReportSchema

from app.utils.product_type_enum import ProductType

router = APIRouter()

@router.get("/", summary="Get product production report for last year")
async def get_all_production():
  report = await Product.find_by_type_with_year(ProductType.PRODUCTION.value, specific_year=2023)
  if not report:
    raise HTTPException(status_code=404, detail="No production products found")
  return report

@router.get("/{year}", summary="Get product production report for a specific year")
async def get_all_production_by_year(year: int):
  report = await Product.find_by_type_with_year(ProductType.PRODUCTION.value, specific_year=year)
  if not report:
    raise HTTPException(status_code=404, detail=f"No production products found for year {year}")
  return report