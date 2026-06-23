"""
KisanMitraAI Cereal Crop Expert Agent

Purpose:
- Provide cereal-specific crop intelligence
- Support rice, wheat, maize, millets and barley
- Feed Crop Planning, Disease, Pest, Weather, Daily Task and Crop Passport agents
"""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class CerealExpertRequest:
    crop: str
    crop_stage: Optional[str] = None
    location: Optional[str] = None
    season: Optional[str] = None


@dataclass
class CerealExpertResult:
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


class CerealCropExpertAgent:

    def __init__(self):
        self.cereal_profiles: Dict[str, Dict] = {
            "rice": {
                "diseases": ["Blast", "Sheath Blight", "Bacterial Leaf Blight", "False Smut"],
                "pests": ["Stem Borer", "Brown Planthopper", "Leaf Folder", "Gall Midge"],
                "nutrition": ["Nitrogen split application", "Zinc", "Phosphorus", "Potassium"],
                "irrigation": ["Maintain field moisture", "Avoid long dry spells", "Drain excess water during disease risk"],
            },
            "wheat": {
                "diseases": ["Yellow Rust", "Brown Rust", "Powdery Mildew", "Karnal Bunt"],
                "pests": ["Aphids", "Termites", "Armyworm"],
                "nutrition": ["Nitrogen split application", "Phosphorus", "Sulphur", "Zinc"],
                "irrigation": ["Critical irrigation at crown root initiation", "Irrigate at booting and grain filling if needed"],
            },
            "maize": {
                "diseases": ["Turcicum Leaf Blight", "Maydis Leaf Blight", "Downy Mildew"],
                "pests": ["Fall Armyworm", "Stem Borer", "Shoot Fly"],
                "nutrition": ["Nitrogen", "Zinc", "Phosphorus", "Potassium"],
                "irrigation": ["Avoid water stress during knee-high, tasseling and grain filling stages"],
            },
            "millet": {
                "diseases": ["Downy Mildew", "Ergot", "Smut"],
                "pests": ["Shoot Fly", "Stem Borer", "Aphids"],
                "nutrition": ["Balanced NPK", "Organic matter", "Micronutrients where deficient"],
                "irrigation": ["Drought tolerant but needs moisture during flowering and grain filling"],
            },
            "barley": {
                "diseases": ["Leaf Rust", "Powdery Mildew", "Net Blotch"],
                "pests": ["Aphids", "Termites"],
                "nutrition": ["Nitrogen management", "Phosphorus", "Sulphur"],
                "irrigation": ["Avoid moisture stress during tillering and grain filling"],
            },
        }

    def advise(self, request: CerealExpertRequest) -> CerealExpertResult:
        crop_key = request.crop.strip().lower()
        profile = self.cereal_profiles.get(crop_key)

        if not profile:
            return CerealExpertResult(
                crop=request.crop,
                matched=False,
                crop_group="Cereal",
                key_diseases=[],
                key_pests=[],
                nutrition_focus=[],
                irrigation_focus=[],
                stage_advice=[
                    "Cereal crop not yet available in expert profile.",
                    "Add this crop to cereal_profiles or crop_registry.json.",
                ],
                next_agents=["crop_expert_router_agent"],
                safety_notes=[
                    "Do not provide crop-specific fertilizer or spray advice until crop is matched.",
                ],
            )

        stage = (request.crop_stage or "general").lower()

        stage_advice = [
            f"Use {request.crop.title()} cereal expert guidance.",
            "Check crop stage, weather, soil moisture and visible symptoms before action.",
        ]

        if "tiller" in stage:
            stage_advice.append("Tillering stage needs nutrition balance and weed monitoring.")
        elif "flower" in stage or "panicle" in stage or "tassel" in stage:
            stage_advice.append("Flowering/panicle/tasseling stage is sensitive to water and pest stress.")
        elif "grain" in stage:
            stage_advice.append("Grain filling stage needs moisture protection and disease monitoring.")
        elif "harvest" in stage:
            stage_advice.append("Harvest stage needs weather check, grain moisture awareness and market planning.")

        return CerealExpertResult(
            crop=request.crop,
            matched=True,
            crop_group="Cereal",
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
    agent = CerealCropExpertAgent()

    result = agent.advise(
        CerealExpertRequest(
            crop="Rice",
            crop_stage="Panicle",
            location="Nadia, West Bengal",
            season="Kharif",
        )
    )

    print(result)
