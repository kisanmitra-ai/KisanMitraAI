"""
KisanMitraAI Crop Planning Agent

Purpose:
- Create crop calendar
- Create day-wise and week-wise crop plan
- Suggest soil preparation
- Suggest fertilizer, irrigation, pest and disease prevention schedule
- Keep advice safety-gated when soil/lab data is missing
"""

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class CropPlanningRequest:
    crop: str
    variety: Optional[str]
    location: str
    season: Optional[str]
    sowing_date: Optional[str]
    area_acres: Optional[float]
    soil_type: Optional[str] = None
    soil_test_available: bool = False


@dataclass
class CropPlanningResult:
    crop: str
    plan_type: str
    soil_preparation: List[str]
    day_wise_plan: List[str]
    fertilizer_plan: List[str]
    irrigation_plan: List[str]
    pest_disease_calendar: List[str]
    safety_notes: List[str]
    next_actions: List[str]


class CropPlanningAgent:

    def create_plan(self, request: CropPlanningRequest) -> CropPlanningResult:
        crop = request.crop

        soil_preparation = [
            "Remove weeds and crop residue before sowing/transplanting.",
            "Check drainage so water does not stay around roots.",
            "Apply well-decomposed compost/FYM if available.",
            "Prepare raised beds or ridges if crop is sensitive to waterlogging.",
        ]

        day_wise_plan = [
            "Day 1: Prepare soil and clean the field.",
            "Day 2: Apply organic matter and level the field.",
            "Day 3: Check soil moisture and prepare seed/seedlings.",
            "Day 4: Create spacing layout as per crop requirement.",
            "Day 5: Sow or transplant healthy seed/seedlings.",
            "Day 6: Give light irrigation if soil is dry.",
            "Day 7: Check germination/plant survival and replace weak plants.",
        ]

        fertilizer_plan = [
            "Use soil test report for exact fertilizer dose.",
            "If soil test is not available, use only general crop-stage guidance.",
            "Apply basal nutrition before sowing/transplanting as per local agronomist guidance.",
            "Split nitrogen application across crop stages instead of applying all at once.",
            "Avoid fertilizer application before heavy rain to reduce nutrient loss.",
        ]

        irrigation_plan = [
            "Keep soil moist during germination or early establishment.",
            "Avoid over-irrigation and waterlogging.",
            "Increase irrigation during flowering and fruiting if crop needs water.",
            "Use weather forecast before irrigation decisions.",
        ]

        pest_disease_calendar = [
            "Week 1-2: Watch for seedling damping-off and early stress.",
            "Week 3-4: Check leaves for spots, curling, insects, and yellowing.",
            "Flowering stage: Monitor pest attack and disease spread closely.",
            "Before harvest: Avoid unsafe chemical spray near harvest window.",
        ]

        safety_notes = [
            "This is a planning estimate, not a certified agronomist prescription.",
            "Exact fertilizer dose requires soil test or local expert validation.",
            "Chemical spray advice must include dose, waiting period, PPE and admin/agronomist review.",
            "Do not guarantee yield, profit, or disease control.",
        ]

        next_actions = [
            "Upload soil test report if available.",
            "Confirm crop variety and sowing/transplanting date.",
            "Connect weather intelligence for dynamic irrigation and spray window.",
            "Connect pest and disease agent for crop-stage risk alerts.",
            "Save this as farmer crop calendar.",
        ]

        return CropPlanningResult(
            crop=crop,
            plan_type="7-day starter crop calendar with safety-gated fertilizer guidance",
            soil_preparation=soil_preparation,
            day_wise_plan=day_wise_plan,
            fertilizer_plan=fertilizer_plan,
            irrigation_plan=irrigation_plan,
            pest_disease_calendar=pest_disease_calendar,
            safety_notes=safety_notes,
            next_actions=next_actions,
        )


if __name__ == "__main__":
    agent = CropPlanningAgent()

    result = agent.create_plan(
        CropPlanningRequest(
            crop="Tomato",
            variety="Local",
            location="Nadia, West Bengal",
            season="Kharif",
            sowing_date="2026-07-01",
            area_acres=1.0,
            soil_type="Alluvial",
            soil_test_available=False,
        )
    )

    print(result)
