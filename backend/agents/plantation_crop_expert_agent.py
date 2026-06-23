"""
KisanMitraAI Plantation Crop Expert Agent
"""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class PlantationExpertRequest:
    crop: str
    crop_stage: Optional[str] = None
    location: Optional[str] = None
    season: Optional[str] = None


@dataclass
class PlantationExpertResult:
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


class PlantationCropExpertAgent:
    def __init__(self):
        self.plantation_profiles: Dict[str, Dict] = {
            "tea": {
                "diseases": ["Blister Blight", "Red Rust", "Grey Blight"],
                "pests": ["Tea Mosquito Bug", "Looper Caterpillar", "Red Spider Mite"],
                "nutrition": ["Nitrogen", "Sulphur", "Organic matter"],
                "irrigation": ["Maintain soil moisture", "Avoid prolonged dry stress"],
            },
            "coffee": {
                "diseases": ["Coffee Leaf Rust", "Berry Disease", "Root Rot"],
                "pests": ["Coffee Berry Borer", "White Stem Borer", "Mealybug"],
                "nutrition": ["Nitrogen", "Potassium", "Calcium"],
                "irrigation": ["Avoid drought stress", "Maintain moisture during berry development"],
            },
            "coconut": {
                "diseases": ["Bud Rot", "Stem Bleeding", "Leaf Spot"],
                "pests": ["Rhinoceros Beetle", "Red Palm Weevil", "Black Headed Caterpillar"],
                "nutrition": ["Potassium", "Boron", "Magnesium"],
                "irrigation": ["Deep irrigation during dry season", "Avoid stagnant water near root zone"],
            },
            "arecanut": {
                "diseases": ["Fruit Rot", "Yellow Leaf Disease", "Bud Rot"],
                "pests": ["Spindle Bug", "Mites", "Root Grubs"],
                "nutrition": ["Potassium", "Magnesium", "Organic matter"],
                "irrigation": ["Maintain moisture year-round", "Ensure drainage during monsoon"],
            },
            "rubber": {
                "diseases": ["Abnormal Leaf Fall", "Powdery Mildew", "Pink Disease"],
                "pests": ["Scale Insects", "Termites", "Leaf Feeders"],
                "nutrition": ["Nitrogen", "Phosphorus", "Potassium"],
                "irrigation": ["Avoid prolonged drought stress"],
            },
            "cocoa": {
                "diseases": ["Black Pod", "Vascular Streak Dieback", "Root Rot"],
                "pests": ["Mirids", "Mealybug", "Stem Borer"],
                "nutrition": ["Potassium", "Calcium", "Organic carbon"],
                "irrigation": ["Consistent moisture required", "Avoid root-zone waterlogging"],
            },
        }

    def advise(self, request: PlantationExpertRequest) -> PlantationExpertResult:
        crop_key = request.crop.strip().lower()
        profile = self.plantation_profiles.get(crop_key)

        if not profile:
            return PlantationExpertResult(
                crop=request.crop,
                matched=False,
                crop_group="Plantation",
                key_diseases=[],
                key_pests=[],
                nutrition_focus=[],
                irrigation_focus=[],
                stage_advice=["Plantation crop not yet available in expert profile."],
                next_agents=["crop_expert_router_agent"],
                safety_notes=["Do not provide crop-specific fertilizer or spray advice until crop is matched."],
            )

        stage = (request.crop_stage or "general").lower()

        stage_advice = [
            f"Use {request.crop.title()} plantation crop expert guidance.",
            "Plantation crops need long-cycle monitoring, soil health, moisture stability and disease surveillance.",
        ]

        if "vegetative" in stage:
            stage_advice.append("Vegetative stage needs canopy health, nutrition balance and pest scouting.")
        elif "flower" in stage or "fruit" in stage or "berry" in stage:
            stage_advice.append("Flowering/fruit/berry stage needs moisture stability and disease monitoring.")
        elif "harvest" in stage:
            stage_advice.append("Harvest stage needs maturity, quality and post-harvest handling checks.")

        return PlantationExpertResult(
            crop=request.crop,
            matched=True,
            crop_group="Plantation",
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
    agent = PlantationCropExpertAgent()
    result = agent.advise(
        PlantationExpertRequest(
            crop="Tea",
            crop_stage="Vegetative",
            location="Darjeeling, West Bengal",
            season="Monsoon",
        )
    )
    print(result)
