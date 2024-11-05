from fastapi import APIRouter, Depends, HTTPException, status
from app.auth.auth import verify_token
from app.models.product_model import Product

from app.utils.product_type_enum import ProductType

router = APIRouter()

@router.get("/", responses={
    404: {"description": "No commercialization products found"},
}, summary="Get product commercialization report for last year")
async def get_all_commercialization(_ = Depends(verify_token)):
  """
  Fetch the commercialization report for the year 2023.
  Args:
      _ (Depends): Dependency to verify the token.
  Returns:
      report (list): List of products for the year 2023.
  Raises:
      HTTPException: If no commercialization products are found, raises a 404 error.
  """
  report = await Product.find_by_type_with_year(ProductType.COMMERCIALIZATION.value, specific_year=2023)
  if not report:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No commercialization products found")
  return report

@router.get("/{year}", responses={
   404: {"description": "No commercialization products found for the given year"},
}, summary="Get product commercialization report for a specific year")
async def get_all_production_by_year(year: int, _ = Depends(verify_token)):
  """
  Fetch the commercialization report for a specified year.
  Args:
      year (int): The year for which to fetch the report.
  Returns:
      report (list): List of products for the specified year.
  Raises:
      HTTPException: If no commercialization products are found for the given year, raises a 404 error.
  """
  report = await Product.find_by_type_with_year(ProductType.COMMERCIALIZATION.value, specific_year=year)
  if not report:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No commercialization products found for year {year}")
  return report