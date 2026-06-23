"""
KisanMitraAI Deal OS Agent

Purpose:
- Match farmers/FPOs with buyers
- Suggest deal structure
- Prepare basic deal terms
"""

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class BuyerMatch:
    buyer_name: str
    buyer_type: str
    location: str
    preferred_grade: str
    offered_price_per_kg: float
    payment_terms: str
    delivery_terms: str
    match_score: int


@dataclass
class DealRequest:
    crop: str
    quantity_kg: float
    location: str
    quality_grade: Optional[str] = "B"
    expected_price_per_kg: Optional[float] = None


@dataclass
class DealResult:
    crop: str
    recommended_buyer: BuyerMatch
    alternative_buyers: List[BuyerMatch]
    suggested_deal_terms: dict
    next_actions: List[str]


class DealOSAgent:

    def match(self, request: DealRequest) -> DealResult:

        buyers = [
            BuyerMatch(
                buyer_name="FreshAgro Retail Buyer",
                buyer_type="Retail Aggregator",
                location="Kolkata",
                preferred_grade="A",
                offered_price_per_kg=23.0,
                payment_terms="70% advance, 30% after delivery confirmation",
                delivery_terms="Farmer/FPO delivers to Kolkata collection point",
                match_score=88,
            ),
            BuyerMatch(
                buyer_name="Nadia Processor Network",
                buyer_type="Processor",
                location="Nadia",
                preferred_grade="B",
                offered_price_per_kg=21.5,
                payment_terms="100% payment within 48 hours of delivery",
                delivery_terms="Buyer pickup from FPO collection center",
                match_score=82,
            ),
            BuyerMatch(
                buyer_name="Krishnanagar Local Trader",
                buyer_type="Trader",
                location="Krishnanagar",
                preferred_grade="B/C",
                offered_price_per_kg=20.5,
                payment_terms="Cash or UPI on delivery",
                delivery_terms="Farmer delivers to local market",
                match_score=76,
            ),
        ]

        grade = (request.quality_grade or "B").upper()

        if grade == "A":
            ranked = sorted(buyers, key=lambda x: (x.match_score, x.offered_price_per_kg), reverse=True)
        elif grade == "C":
            ranked = sorted(buyers, key=lambda x: x.delivery_terms.startswith("Buyer pickup"), reverse=True)
        else:
            ranked = sorted(buyers, key=lambda x: x.match_score, reverse=True)

        recommended = ranked[0]

        suggested_terms = {
            "crop": request.crop,
            "quantity_kg": request.quantity_kg,
            "quality_grade": grade,
            "price_band_per_kg": f"₹{recommended.offered_price_per_kg - 0.75:.2f} - ₹{recommended.offered_price_per_kg:.2f}",
            "payment_terms": recommended.payment_terms,
            "delivery_terms": recommended.delivery_terms,
            "quality_tolerance": "Up to 5% minor defects allowed unless buyer requires Grade A strict sorting.",
            "recommended_contract_type": "Simple produce sale agreement",
        }

        return DealResult(
            crop=request.crop,
            recommended_buyer=recommended,
            alternative_buyers=ranked[1:],
            suggested_deal_terms=suggested_terms,
            next_actions=[
                "Create deal request with recommended buyer.",
                "Confirm quantity, grade and harvest date.",
                "Confirm transport or pickup arrangement.",
                "Generate simple sale agreement before dispatch.",
                "Run Trust Engine before final confirmation.",
            ],
        )


if __name__ == "__main__":
    agent = DealOSAgent()

    result = agent.match(
        DealRequest(
            crop="Tomato",
            quantity_kg=1000,
            location="Nadia, West Bengal",
            quality_grade="A",
            expected_price_per_kg=22.5,
        )
    )

    print(result)
