"""
KisanMitraAI Spice Crop Expert Agent
"""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class SpiceExpertRequest:
    crop: str
    crop_stage: Optional[str] = None
    location: Optional[str] = None
    season: Optional[str] = None


@dataclass
class SpiceExpertResult:
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


class SpiceCropExpertAgent:
    def __init__(self):
        self.spice_profiles: Dict[str, Dict] = {
            "turmeric": {
                "diseases": ["Rhizome Rot", "Leaf Blotch", "Leaf Spot"],
                "pests": ["Shoot Borer", "Rhizome Scale"],
                "nutrition": ["Potassium", "Organic matter", "Sulphur"],
                "irrigation": ["Avoid waterlogging", "Maintain uniform moisture"],
            },
            "ginger": {
                "diseases": ["Soft Rot", "Bacterial Wilt", "Leaf Spot"],
                "pests": ["Shoot Borer", "Nematodes", "Rhizome Scale"],
                "nutrition": ["Potassium", "Organic carbon", "Sulphur"],
                "irrigation": ["Good drainage required", "Avoid standing water"],
            },
            "chilli": {
                "diseases": ["Anthracnose", "Wilt", "Leaf Curl Virus"],
                "pests": ["Thrips", "Mites", "Fruit Borer"],
                "nutrition": ["Calcium", "Potassium", "Boron"],
                "irrigation": ["Avoid moisture stress", "Avoid waterlogging"],
            },
            "coriander": {
                "diseases": ["Powdery Mildew", "Stem Gall", "Wilt"],
                "pests": ["Aphids", "Cutworm"],
                "nutrition": ["Nitrogen balance", "Phosphorus", "Organic matter"],
                "irrigation": ["Light irrigation", "Avoid excess moisture"],
            },
            "cumin": {
                "diseases": ["Wilt", "Blight", "Powdery Mildew"],
                "pests": ["Aphids", "Thrips"],
                "nutrition": ["Phosphorus", "Sulphur", "Organic matter"],
                "irrigation": ["Avoid waterlogging", "Use controlled irrigation"],
            },
            "black pepper": {
                "diseases": ["Quick Wilt", "Slow Decline", "Leaf Rot"],
                "pests": ["Pollu Beetle", "Scale Insects", "Mealybug"],
                "nutrition": ["Organic matter", "Potassium", "Magnesium"],
                "irrigation": ["Maintain moisture", "Avoid root-zone waterlogging"],
            },
            "cardamom": {
                "diseases": ["Katte Disease", "Rhizome Rot", "Leaf Blight"],
                "pests": ["Thrips", "Shoot Borer", "Aphids"],
                "nutrition": ["Organic matter", "Potassium", "Magnesium"],
                "irrigation": ["Maintain humid conditions", "Avoid stagnant water"],
            },
        }

    def advise(self, request: SpiceExpertRequest) -> SpiceExpertResult:
        crop_key = request.crop.strip().lower()
        profile = self.spice_profiles.get(crop_key)

        if not profile:
            return SpiceExpertResult(
                crop=request.crop,
                matched=False,
                crop_group="Spice",
                key_diseases=[],
                key_pests=[],
                nutrition_focus=[],
                irrigation_focus=[],
                stage_advice=["Spice crop not yet available in expert profile."],
                next_agents=["crop_expert_router_agent"],
                safety_notes=["Do not provide crop-specific fertilizer or spray advice until crop is matched."],
            )

        stage = (request.crop_stage or "general").lower()

        stage_advice = [
            f"Use {request.crop.title()} spice crop expert guidance.",
            "Spice crops need strong moisture, drainage, disease monitoring and post-harvest quality control.",
        ]

        if "vegetative" in stage:
            stage_advice.append("Vegetative stage needs healthy root/rhizome growth and balanced nutrition.")
        elif "flower" in stage or "fruit" in stage:
            stage_advice.append("Flowering/fruiting stage needs pest monitoring and moisture stability.")
        elif "harvest" in stage:
            stage_advice.append("Harvest stage needs maturity check, safe drying and storage guidance.")

        return SpiceExpertResult(
            crop=request.crop,
            matched=True,
            crop_group="Spice",
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
    agent = SpiceCropExpertAgent()
    result = agent.advise(
        SpiceExpertRequest(
            crop="Turmeric",
            crop_stage="Vegetative",
            location="Nadia, West Bengal",
            season="Kharif",
        )
    )
    print(result)
