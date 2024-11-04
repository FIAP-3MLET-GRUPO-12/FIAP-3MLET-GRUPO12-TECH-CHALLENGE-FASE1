from typing import Dict, Literal
from fastapi import APIRouter, Depends, HTTPException, status
from app.auth.auth import verify_token
from app.models.product_model import Product
from app.schemas.product_report_schema import ProductReportSchema
from app.utils.product_type_enum import ProductType

router = APIRouter()

@router.get("/{processing_category}", responses={
    404: {"description": "No processing products found for the given category"},
}, summary="Get Processing report for last year", )
async def get_processing_report(processing_category: Literal[
        ProductType.PROCESSING_AMERICAN.value, # type: ignore
        ProductType.PROCESSING_TABLE_GRAPES.value, # type: ignore
        ProductType.PROCESSING_UNRATED.value, # type: ignore
        ProductType.PROCESSING_VINES.value # type: ignore
    ], _ = Depends(verify_token)):
    """
    Get the processing report for the last year for a given category.

    Args:
        processing_category (Literal): The category of processing products. 
            Must be one of the following:
            - processing_american
            - processing_table_grapes
            - processing_unrated
            - processing_vines

    Returns:
        report: The processing report for the last year.

    Raises:
        HTTPException: If no processing products are found for the given category.
    """
    report = await Product.find_by_type_with_year(processing_category, specific_year=2023)
    if not report:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No processing products found for category {processing_category}")
    return report

@router.get("/{processing_category}/{year}",responses={
    404: {"description": "No processing products found for the given category and year"},
}, summary="Get Processing report for a specific year")
async def get_processing_report_by_year(processing_category: Literal[
        ProductType.PROCESSING_AMERICAN.value, # type: ignore
        ProductType.PROCESSING_TABLE_GRAPES.value, # type: ignore
        ProductType.PROCESSING_UNRATED.value, # type: ignore
        ProductType.PROCESSING_VINES.value # type: ignore
    ], year: int, _ = Depends(verify_token)):
    """
    Get the processing report for a specific year for a given category.

    Args:
        processing_category (Literal): The category of processing products. 
            Must be one of the following:
            - processing_american
            - processing_table_grapes
            - processing_unrated
            - processing_vines
        year (int): The specific year for which the report is requested.

    Returns:
        report: The processing report for the specified year.

    Raises:
        HTTPException: If no processing products are found for the given category and year.
    """
    report = await Product.find_by_type_with_year(processing_category, specific_year=year)
    if not report:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No processing products found for category {processing_category} and year {year}")
    return report