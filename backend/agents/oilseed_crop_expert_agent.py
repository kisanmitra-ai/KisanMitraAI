"""
KisanMitraAI Oilseed Crop Expert Agent
"""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class OilseedExpertRequest:
    crop: str
    crop_stage: Optional[str] = None
    location: Optional[str] = None
    season: Optional[str] = None


@dataclass
class OilseedExpertResult:
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


class OilseedCropExpertAgent:
    def __init__(self):
        self.oilseed_profiles: Dict[str, Dict] = {
            "mustard": {
                "diseases": ["White Rust", "Alternaria Blight", "Downy Mildew"],
                "pests": ["Aphids", "Painted Bug", "Sawfly"],
                "nutrition": ["Sulphur", "Boron", "Nitrogen split application", "Phosphorus"],
                "irrigation": ["Avoid waterlogging", "Critical moisture during flowering and pod filling"],
            },
            "groundnut": {
                "diseases": ["Tikka Leaf Spot", "Rust", "Collar Rot", "Stem Rot"],
                "pests": ["Leaf Miner", "Aphids", "White Grub", "Thrips"],
                "nutrition": ["Calcium", "Sulphur", "Phosphorus", "Organic matter"],
                "irrigation": ["Avoid drought during pegging and pod development", "Avoid excess water"],
            },
            "soybean": {
                "diseases": ["Rust", "Yellow Mosaic Virus", "Charcoal Rot", "Bacterial Pustule"],
                "pests": ["Stem Fly", "Girdle Beetle", "Semilooper", "Aphids"],
                "nutrition": ["Rhizobium", "Phosphorus", "Sulphur", "Potassium"],
                "irrigation": ["Avoid waterlogging", "Protect moisture during flowering and pod filling"],
            },
            "sesame": {
                "diseases": ["Phyllody", "Leaf Spot", "Root Rot"],
                "pests": ["Leaf Webber", "Capsule Borer", "Aphids"],
                "nutrition": ["Sulphur", "Phosphorus", "Organic matter"],
                "irrigation": ["Low water crop, avoid waterlogging, protect flowering stage"],
            },
            "sunflower": {
                "diseases": ["Alternaria Leaf Spot", "Downy Mildew", "Rust", "Sclerotinia Rot"],
                "pests": ["Head Borer", "Aphids", "Jassids"],
                "nutrition": ["Boron", "Sulphur", "Potassium", "Balanced Nitrogen"],
                "irrigation": ["Critical irrigation at flowering and seed filling"],
            },
            "castor": {
                "diseases": ["Wilt", "Root Rot", "Alternaria Blight"],
                "pests": ["Semi Looper", "Capsule Borer", "Aphids"],
                "nutrition": ["Nitrogen", "Phosphorus", "Organic matter"],
                "irrigation": ["Avoid waterlogging, protect crop during flowering and capsule development"],
            },
        }

    def advise(self, request: OilseedExpertRequest) -> OilseedExpertResult:
        crop_key = request.crop.strip().lower()
        profile = self.oilseed_profiles.get(crop_key)

        if not profile:
            return OilseedExpertResult(
                crop=request.crop,
                matched=False,
                crop_group="Oilseed",
                key_diseases=[],
                key_pests=[],
                nutrition_focus=[],
                irrigation_focus=[],
                stage_advice=["Oilseed crop not yet available in expert profile."],
                next_agents=["crop_expert_router_agent"],
                safety_notes=["Do not provide crop-specific fertilizer or spray advice until crop is matched."],
            )

        stage = (request.crop_stage or "general").lower()

        stage_advice = [
            f"Use {request.crop.title()} oilseed crop expert guidance.",
            "Oilseed crops need careful moisture, sulphur/boron awareness and pest monitoring.",
        ]

        if "flower" in stage:
            stage_advice.append("Flowering stage needs moisture stability and aphid/pest scouting.")
        elif "pod" in stage or "seed" in stage or "capsule" in stage:
            stage_advice.append("Seed/pod/capsule filling stage is important for oil content and final yield.")
        elif "harvest" in stage:
            stage_advice.append("Harvest stage needs maturity check and safe drying/storage moisture.")

        return OilseedExpertResult(
            crop=request.crop,
            matched=True,
            crop_group="Oilseed",
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
    agent = OilseedCropExpertAgent()
    result = agent.advise(
        OilseedExpertRequest(
            crop="Mustard",
            crop_stage="Flowering",
            location="Nadia, West Bengal",
            season="Rabi",
        )
    )
    print(result)
