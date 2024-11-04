from typing import Dict, Literal
from fastapi import APIRouter, HTTPException
from app.models.product_model import Product
from app.schemas.product_report_schema import ProductReportSchema
from app.utils.product_type_enum import ProductType

router = APIRouter()

@router.get("/{processing_category}", summary="Get Processing report for last year", )
async def get_processing_report(processing_category: Literal[
        ProductType.PROCESSING_AMERICAN.value, # type: ignore
        ProductType.PROCESSING_TABLE_GRAPES.value, # type: ignore
        ProductType.PROCESSING_UNRATED.value, # type: ignore
        ProductType.PROCESSING_VINES.value # type: ignore
    ]):
   
    report = await Product.find_by_type_with_year(processing_category, specific_year=2023)
    if not report:
        raise HTTPException(status_code=404, detail=f"No processing products found for category {processing_category}")
    return report

@router.get("/{processing_category}/{year}", summary="Get Processing report for a specific year")
async def get_processing_report_by_year(processing_category: Literal[
        ProductType.PROCESSING_AMERICAN.value, # type: ignore
        ProductType.PROCESSING_TABLE_GRAPES.value, # type: ignore
        ProductType.PROCESSING_UNRATED.value, # type: ignore
        ProductType.PROCESSING_VINES.value # type: ignore
    ], year: int):
   
    report = await Product.find_by_type_with_year(processing_category, specific_year=year)
    if not report:
        raise HTTPException(status_code=404, detail=f"No processing products found for category {processing_category} and year {year}")
    return report