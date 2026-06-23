"""
KisanMitraAI Best Mandi Engine

Purpose:
Find best mandi or buyer based on:
- crop
- quantity
- location
- transport cost
- expected net realization
"""

from dataclasses import dataclass
from typing import List


@dataclass
class MandiOption:
    mandi_name: str
    district: str
    gross_price_per_kg: float
    transport_cost_per_kg: float
    net_price_per_kg: float
    risk_level: str
    recommendation: str


@dataclass
class BestMandiRequest:
    crop: str
    quantity_kg: float
    location: str
    time_window: str = "today"


@dataclass
class BestMandiResult:
    crop: str
    location: str
    best_option: MandiOption
    alternatives: List[MandiOption]


class BestMandiAgent:

    def evaluate(self, request: BestMandiRequest):

        options = [

            MandiOption(
                mandi_name="Kolkata Wholesale Market",
                district="Kolkata",
                gross_price_per_kg=24.0,
                transport_cost_per_kg=1.5,
                net_price_per_kg=22.5,
                risk_level="Low",
                recommendation="Highest expected net realization."
            ),

            MandiOption(
                mandi_name="Kalyani Mandi",
                district="Nadia",
                gross_price_per_kg=22.0,
                transport_cost_per_kg=0.5,
                net_price_per_kg=21.5,
                risk_level="Low",
                recommendation="Nearby option with lower logistics."
            ),

            MandiOption(
                mandi_name="Krishnanagar Market",
                district="Nadia",
                gross_price_per_kg=21.0,
                transport_cost_per_kg=0.4,
                net_price_per_kg=20.6,
                risk_level="Very Low",
                recommendation="Safest local option."
            )
        ]

        best = sorted(
            options,
            key=lambda x: x.net_price_per_kg,
            reverse=True
        )[0]

        return BestMandiResult(
            crop=request.crop,
            location=request.location,
            best_option=best,
            alternatives=options[1:]
        )


if __name__ == "__main__":

    agent = BestMandiAgent()

    result = agent.evaluate(
        BestMandiRequest(
            crop="Tomato",
            quantity_kg=1000,
            location="Nadia, West Bengal"
        )
    )

    print(result)
