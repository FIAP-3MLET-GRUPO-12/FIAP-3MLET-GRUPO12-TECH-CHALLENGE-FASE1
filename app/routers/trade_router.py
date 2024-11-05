from typing import Literal
from fastapi import APIRouter, Depends, HTTPException, status

from app.auth.auth import verify_token
from app.models.trade_model import Trade
from app.utils.trade_type_enum import TradeDerivatives

router = APIRouter()

@router.get("/import/{derivative}", summary="Get import trades by derivative")
async def get_trades(derivative: Literal[
        TradeDerivatives.TABLE_WINES.value, # type: ignore
        TradeDerivatives.SPARKLING_WINES.value, # type: ignore
        TradeDerivatives.FRASH_GRAPES.value, # type: ignore
        TradeDerivatives.GRAPE_JUICE.value, # type: ignore
        TradeDerivatives.RAISINS.value # type: ignore
    ],
    # token: str = Depends(verify_token),
    ):
    report = await Trade.find_by_derivative_with_year(derivative=derivative, specific_year=2023, type_value="import")
    
    if not report:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No trades found for derivative {derivative}")
    
    return report

@router.get("/import/{derivative}/{year}", summary="Get import trades by derivative and year")
async def get_trades(derivative: Literal[
        TradeDerivatives.TABLE_WINES.value, # type: ignore
        TradeDerivatives.SPARKLING_WINES.value, # type: ignore
        TradeDerivatives.FRASH_GRAPES.value, # type: ignore
        TradeDerivatives.GRAPE_JUICE.value, # type: ignore
        TradeDerivatives.RAISINS.value # type: ignore
    ],
    year: int,
    # token: str = Depends(verify_token),
    ):
    report = await Trade.find_by_derivative_with_year(derivative=derivative, specific_year=year, type_value="import")
    
    if not report:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No trades found for derivative {derivative}")
    
    return report

@router.get("/export/{derivative}", summary="Get export trades by derivative")
async def get_trades(derivative: Literal[
        TradeDerivatives.TABLE_WINES.value, # type: ignore
        TradeDerivatives.SPARKLING_WINES.value, # type: ignore
        TradeDerivatives.FRASH_GRAPES.value, # type: ignore
        TradeDerivatives.GRAPE_JUICE.value # type: ignore
    ],
    # token: str = Depends(verify_token),
    ):
    report = await Trade.find_by_derivative_with_year(derivative=derivative, specific_year=2023, type_value="export")
    
    if not report:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No trades found for derivative {derivative}")
    
    return report

@router.get("/export/{derivative}/{year}", summary="Get export trades by derivative and year")
async def get_trades(derivative: Literal[
        TradeDerivatives.TABLE_WINES.value, # type: ignore
        TradeDerivatives.SPARKLING_WINES.value, # type: ignore
        TradeDerivatives.FRASH_GRAPES.value, # type: ignore
        TradeDerivatives.GRAPE_JUICE.value # type: ignore
    ],
    year: int,
    # token: str = Depends(verify_token),
    ):
    report = await Trade.find_by_derivative_with_year(derivative=derivative, specific_year=year, type_value="export")
    
    if not report:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No trades found for derivative {derivative}")
    
    return report
    