import uuid
from typing import List, Optional

from pydantic import BaseModel


# Shared properties
class FinancialPerformanceBase(BaseModel):
    id: Optional[uuid.UUID]
    who: Optional[str]
    main_revenue_sources: Optional[str]
    other_revenue_sources: Optional[str]
    ppa_period: Optional[int]
    power_sales_period: Optional[int]
    average_annual_output: Optional[float]
    tariff_price: Optional[float]
    average_annual_revenue: Optional[float]
    total_revenue: Optional[float]
    discounted_benefits: Optional[float]
    discounted_costs: Optional[float]
    capital_investment: Optional[float]
    capital_cost_percentage: Optional[float]
    payback_period: Optional[int]
    npv: Optional[float]
    average_annual_cashflow: Optional[float]
    average_annual_costs: Optional[float]
    average_annual_expenses: Optional[float]
    total_annual_costs: Optional[float]
    applicable_cost_period: Optional[int]
    total_costs_period: Optional[int]
    total_net_revenue: Optional[float]
    average_annual_net_revenue: Optional[float]
    key_model_results: Optional[str]


class FinancialPerformanceUpdate(FinancialPerformanceBase):
    pass


# Properties to receive via API on creation
class FinancialPerformanceCreate(FinancialPerformanceBase):
    pass


class FinancialPerformanceInDBBase(FinancialPerformanceBase):
    id: uuid.UUID

    class Config:
        orm_mode = True


# Additional properties to return via API
class FinancialPerformance(FinancialPerformanceInDBBase):
    pass


# Additional properties stored in DB
class FinancialPerformanceInDB(FinancialPerformanceInDBBase):
    pass


class FinancialPerformanceResponse(BaseModel):
    success: bool
    data: Optional[FinancialPerformance]


class FinancialPerformanceListResponse(BaseModel):
    success: bool
    data: Optional[List[FinancialPerformance]]
