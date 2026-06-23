"""
KisanMitraAI Vegetable Crop Expert Agent

Purpose:
- Provide vegetable-specific crop intelligence
- Support tomato, potato, onion, chilli, brinjal, okra, cabbage, cauliflower, gourds and cucumber
- Feed Crop Planning, Disease, Pest, Weather, Daily Task and Crop Passport agents
"""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class VegetableExpertRequest:
    crop: str
    crop_stage: Optional[str] = None
    location: Optional[str] = None
    season: Optional[str] = None


@dataclass
class VegetableExpertResult:
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


class VegetableCropExpertAgent:

    def __init__(self):
        self.vegetable_profiles: Dict[str, Dict] = {
            "tomato": {
                "diseases": ["Early Blight", "Late Blight", "Bacterial Spot", "Leaf Curl Virus"],
                "pests": ["Whitefly", "Fruit Borer", "Aphids", "Thrips"],
                "nutrition": ["Calcium", "Potassium", "Balanced Nitrogen", "Micronutrients"],
                "irrigation": ["Avoid waterlogging", "Maintain even moisture", "Reduce leaf wetness"],
            },
            "potato": {
                "diseases": ["Late Blight", "Early Blight", "Black Scurf"],
                "pests": ["Aphids", "Cutworm", "Potato Tuber Moth"],
                "nutrition": ["Potassium", "Phosphorus", "Balanced Nitrogen"],
                "irrigation": ["Avoid waterlogging", "Maintain ridge moisture", "Reduce stress during tuber formation"],
            },
            "onion": {
                "diseases": ["Purple Blotch", "Downy Mildew", "Basal Rot"],
                "pests": ["Thrips", "Cutworm"],
                "nutrition": ["Sulphur", "Potassium", "Nitrogen split application"],
                "irrigation": ["Avoid excess water", "Reduce irrigation before harvest", "Support bulb formation"],
            },
            "chilli": {
                "diseases": ["Anthracnose", "Leaf Curl Virus", "Powdery Mildew"],
                "pests": ["Thrips", "Mites", "Aphids"],
                "nutrition": ["Potassium", "Calcium", "Micronutrients"],
                "irrigation": ["Avoid moisture stress", "Avoid waterlogging", "Maintain regular irrigation"],
            },
            "brinjal": {
                "diseases": ["Phomopsis Blight", "Bacterial Wilt", "Little Leaf"],
                "pests": ["Shoot and Fruit Borer", "Aphids", "Jassids"],
                "nutrition": ["Nitrogen split application", "Potassium", "Organic matter"],
                "irrigation": ["Maintain moisture during flowering and fruiting"],
            },
            "okra": {
                "diseases": ["Yellow Vein Mosaic Virus", "Powdery Mildew"],
                "pests": ["Jassids", "Aphids", "Fruit Borer"],
                "nutrition": ["Balanced NPK", "Organic matter"],
                "irrigation": ["Avoid water stress during flowering"],
            },
            "cabbage": {
                "diseases": ["Black Rot", "Downy Mildew", "Clubroot"],
                "pests": ["Diamondback Moth", "Aphids", "Cabbage Caterpillar"],
                "nutrition": ["Nitrogen", "Boron", "Calcium"],
                "irrigation": ["Maintain uniform soil moisture"],
            },
            "cauliflower": {
                "diseases": ["Black Rot", "Downy Mildew", "Clubroot"],
                "pests": ["Diamondback Moth", "Aphids", "Cabbage Caterpillar"],
                "nutrition": ["Boron", "Molybdenum", "Calcium"],
                "irrigation": ["Avoid stress during curd formation"],
            },
            "cucumber": {
                "diseases": ["Downy Mildew", "Powdery Mildew", "Mosaic Virus"],
                "pests": ["Fruit Fly", "Aphids", "Whitefly"],
                "nutrition": ["Potassium", "Calcium", "Balanced Nitrogen"],
                "irrigation": ["Maintain regular moisture", "Avoid leaf wetness"],
            },
            "bottle gourd": {
                "diseases": ["Downy Mildew", "Powdery Mildew", "Anthracnose"],
                "pests": ["Fruit Fly", "Red Pumpkin Beetle", "Aphids"],
                "nutrition": ["Organic matter", "Potassium", "Balanced NPK"],
                "irrigation": ["Regular irrigation during vine growth and fruiting"],
            },
        }

    def advise(self, request: VegetableExpertRequest) -> VegetableExpertResult:
        crop_key = request.crop.strip().lower()
        profile = self.vegetable_profiles.get(crop_key)

        if not profile:
            return VegetableExpertResult(
                crop=request.crop,
                matched=False,
                crop_group="Vegetable",
                key_diseases=[],
                key_pests=[],
                nutrition_focus=[],
                irrigation_focus=[],
                stage_advice=[
                    "Vegetable crop not yet available in expert profile.",
                    "Add this crop to vegetable_profiles or crop_registry.json.",
                ],
                next_agents=["crop_expert_router_agent"],
                safety_notes=[
                    "Do not provide crop-specific fertilizer or spray advice until crop is matched.",
                ],
            )

        stage = (request.crop_stage or "general").lower()

        stage_advice = [
            f"Use {request.crop.title()} vegetable expert guidance.",
            "Check crop stage, weather, soil moisture and visible symptoms before action.",
        ]

        if "flower" in stage or "fruit" in stage:
            stage_advice.append("Flowering/fruiting stage needs close pest monitoring and balanced nutrition.")
        elif "nursery" in stage or "seedling" in stage:
            stage_advice.append("Seedling stage needs drainage, damping-off prevention and gentle irrigation.")
        elif "harvest" in stage:
            stage_advice.append("Harvest stage needs residue safety, quality grading and market planning.")

        return VegetableExpertResult(
            crop=request.crop,
            matched=True,
            crop_group="Vegetable",
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
                "Fertilizer dosage must use soil test or local agronomist validation.",
                "Chemical spray recommendation must include dose, waiting period, PPE and safety review.",
                "This expert output is advisory and should be confidence-scored before farmer-facing release.",
            ],
        )


if __name__ == "__main__":
    agent = VegetableCropExpertAgent()

    result = agent.advise(
        VegetableExpertRequest(
            crop="Tomato",
            crop_stage="Flowering",
            location="Nadia, West Bengal",
            season="Kharif",
        )
    )

    print(result)
