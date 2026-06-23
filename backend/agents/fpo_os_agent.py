"""
KisanMitraAI FPO OS Agent

Purpose:
- Manage FPO operations
- Maintain farmer records
- Create aggregation lots
- Track collection, payments and account books
"""

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class FarmerMember:
    farmer_id: str
    farmer_name: str
    village: str
    mobile: str
    crop: str
    expected_quantity_kg: float


@dataclass
class AggregationLot:
    lot_id: str
    crop: str
    total_quantity_kg: float
    farmers_count: int
    quality_grade: str
    status: str


@dataclass
class FPORequest:
    fpo_name: str
    operation_type: str
    crop: Optional[str] = None
    location: Optional[str] = None


@dataclass
class FPOResult:
    fpo_name: str
    operation_type: str
    summary: str
    farmer_members: List[FarmerMember]
    aggregation_lot: Optional[AggregationLot]
    account_actions: List[str]
    next_actions: List[str]


class FPOOSAgent:

    def manage(self, request: FPORequest) -> FPOResult:
        farmers = [
            FarmerMember(
                farmer_id="KM-FARMER-001",
                farmer_name="Ranjan Test Farmer",
                village="Basbona",
                mobile="Hidden for privacy",
                crop=request.crop or "Tomato",
                expected_quantity_kg=500,
            ),
            FarmerMember(
                farmer_id="KM-FARMER-002",
                farmer_name="Sample Farmer 2",
                village="Nadia",
                mobile="Hidden for privacy",
                crop=request.crop or "Tomato",
                expected_quantity_kg=700,
            ),
        ]

        total_quantity = sum(f.expected_quantity_kg for f in farmers)

        aggregation_lot = AggregationLot(
            lot_id="KM-LOT-0001",
            crop=request.crop or "Tomato",
            total_quantity_kg=total_quantity,
            farmers_count=len(farmers),
            quality_grade="B",
            status="Draft aggregation lot ready",
        )

        summary = (
            f"{request.fpo_name} can aggregate {total_quantity} kg "
            f"of {aggregation_lot.crop} from {len(farmers)} farmers."
        )

        return FPOResult(
            fpo_name=request.fpo_name,
            operation_type=request.operation_type,
            summary=summary,
            farmer_members=farmers,
            aggregation_lot=aggregation_lot,
            account_actions=[
                "Create farmer-wise payable ledger.",
                "Record collection center receipt.",
                "Track buyer payment against lot.",
                "Split final payment farmer-wise after deductions.",
            ],
            next_actions=[
                "Confirm farmer quantities.",
                "Run Quality Grading Agent for lot.",
                "Run Best Mandi Agent for price comparison.",
                "Run Deal OS Agent for buyer matching.",
                "Run Trust Engine before dispatch.",
            ],
        )


if __name__ == "__main__":
    agent = FPOOSAgent()

    result = agent.manage(
        FPORequest(
            fpo_name="Nadia Sample FPO",
            operation_type="aggregation",
            crop="Tomato",
            location="Nadia, West Bengal",
        )
    )

    print(result)
