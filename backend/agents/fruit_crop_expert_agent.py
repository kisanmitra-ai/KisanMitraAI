"""
KisanMitraAI Fruit Crop Expert Agent
"""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class FruitExpertRequest:
    crop: str
    crop_stage: Optional[str] = None
    location: Optional[str] = None
    season: Optional[str] = None


@dataclass
class FruitExpertResult:
    crop: str
    matched: bool
    crop_group: str
    key_diseases: List[str]
    key_pests: List[str]
    nutrition_focus: List[str]
    irrigation_focus: List[str]
    stage_advice: List[str]
    next_agents: List[str]
    safety_notes: List[str]


class FruitCropExpertAgent:
    def __init__(self):
        self.fruit_profiles: Dict[str, Dict] = {
            "mango": {
                "diseases": ["Anthracnose", "Powdery Mildew", "Dieback"],
                "pests": ["Mango Hopper", "Fruit Fly", "Mealybug"],
                "nutrition": ["Potassium", "Calcium", "Boron", "Balanced Nitrogen"],
                "irrigation": ["Avoid water stress during flowering", "Reduce excess moisture near harvest"],
            },
            "banana": {
                "diseases": ["Sigatoka Leaf Spot", "Panama Wilt", "Bunchy Top Virus"],
                "pests": ["Rhizome Weevil", "Nematodes", "Aphids"],
                "nutrition": ["Potassium", "Nitrogen", "Magnesium", "Organic matter"],
                "irrigation": ["Maintain regular moisture", "Avoid waterlogging"],
            },
            "guava": {
                "diseases": ["Anthracnose", "Wilt", "Fruit Rot"],
                "pests": ["Fruit Fly", "Mealybug", "Scale Insects"],
                "nutrition": ["Potassium", "Zinc", "Boron"],
                "irrigation": ["Avoid stress during flowering and fruit development"],
            },
            "papaya": {
                "diseases": ["Papaya Ring Spot Virus", "Anthracnose", "Root Rot"],
                "pests": ["Aphids", "Whitefly", "Mealybug"],
                "nutrition": ["Nitrogen", "Potassium", "Calcium"],
                "irrigation": ["Avoid waterlogging", "Maintain consistent moisture"],
            },
            "litchi": {
                "diseases": ["Fruit Rot", "Anthracnose", "Leaf Spot"],
                "pests": ["Fruit Borer", "Litchi Mite", "Mealybug"],
                "nutrition": ["Potassium", "Boron", "Zinc"],
                "irrigation": ["Maintain moisture during fruit development"],
            },
            "citrus": {
                "diseases": ["Citrus Canker", "Gummosis", "Greening"],
                "pests": ["Citrus Psylla", "Leaf Miner", "Aphids"],
                "nutrition": ["Zinc", "Iron", "Magnesium", "Nitrogen"],
                "irrigation": ["Avoid waterlogging", "Maintain moisture during fruit set"],
            },
            "pomegranate": {
                "diseases": ["Bacterial Blight", "Fruit Rot", "Wilt"],
                "pests": ["Fruit Borer", "Thrips", "Aphids"],
                "nutrition": ["Potassium", "Calcium", "Boron"],
                "irrigation": ["Avoid irregular irrigation during fruit development"],
            },
        }

    def advise(self, request: FruitExpertRequest) -> FruitExpertResult:
        crop_key = request.crop.strip().lower()
        profile = self.fruit_profiles.get(crop_key)

        if not profile:
            return FruitExpertResult(
                crop=request.crop,
                matched=False,
                crop_group="Fruit",
                key_diseases=[],
                key_pests=[],
                nutrition_focus=[],
                irrigation_focus=[],
                stage_advice=["Fruit crop not yet available in expert profile."],
                next_agents=["crop_expert_router_agent"],
                safety_notes=["Do not provide crop-specific fertilizer or spray advice until crop is matched."],
            )

        stage = (request.crop_stage or "general").lower()

        stage_advice = [
            f"Use {request.crop.title()} fruit crop expert guidance.",
            "Check flowering, fruit set, weather, irrigation and visible symptoms before action.",
        ]

        if "flower" in stage:
            stage_advice.append("Flowering stage needs moisture balance, pollination support and pest monitoring.")
        elif "fruit" in stage:
            stage_advice.append("Fruit development stage needs potassium, calcium and disease monitoring.")
        elif "harvest" in stage:
            stage_advice.append("Harvest stage needs maturity check, residue safety and quality grading.")

        return FruitExpertResult(
            crop=request.crop,
            matched=True,
            crop_group="Fruit",
            key_diseases=profile["diseases"],
            key_pests=profile["pests"],
            nutrition_focus=profile["nutrition"],
            irrigation_focus=profile["irrigation"],
            stage_advice=stage_advice,
            next_agents=[
                "weather_intelligence_agent",
                "disease_detection_agent",
                "pest_detection_agent",
                "plant_stress_agent",
                "crop_planning_agent",
                "daily_task_engine",
                "crop_passport_agent",
            ],
            safety_notes=[
                "Fertilizer dose must use soil test or local agronomist validation.",
                "Chemical spray recommendation must include dose, waiting period, PPE and safety review.",
                "This expert output is advisory and should be confidence-scored before farmer-facing release.",
            ],
        )


if __name__ == "__main__":
    agent = FruitCropExpertAgent()
    result = agent.advise(
        FruitExpertRequest(
            crop="Mango",
            crop_stage="Flowering",
            location="Nadia, West Bengal",
            season="Summer",
        )
    )
    print(result)
