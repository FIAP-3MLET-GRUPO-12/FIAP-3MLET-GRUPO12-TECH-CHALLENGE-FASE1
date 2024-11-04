from fastapi import APIRouter, Depends, HTTPException, status
from app.auth.auth import verify_token
from app.models.product_model import Product
from app.schemas.product_report_schema import ProductReportSchema

from app.utils.product_type_enum import ProductType

router = APIRouter()

@router.get("/", responses={
    404: {"description": "No production products found"},
},summary="Get product production report for last year")
async def get_all_production(_ = Depends(verify_token)):
  """
  Retrieves the production product report for the last year.
  Args:
  - _: Dependency that verifies the token.
  Returns:
  - The production product report for the last year.
  Raises:
  - HTTPException: If no production products are found.
  """
  report = await Product.find_by_type_with_year(ProductType.PRODUCTION.value, specific_year=2023)
  if not report:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No production products found")
  return report

@router.get("/{year}", responses={
    404: {"description": "No production products found for the given year"},
}, summary="Get product production report for a specific year")
async def get_all_production_by_year(year: int, _ = Depends(verify_token)):
  """
  Retrieves the production product report for a specific year.
  Args:
  - year: The year for which the production product report is to be retrieved.
  Returns:
  - The production product report for the specified year.
  Raises:
  - HTTPException: If no production products are found for the given year.
  """
  report = await Product.find_by_type_with_year(ProductType.PRODUCTION.value, specific_year=year)
  if not report:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No production products found for year {year}")
  return report