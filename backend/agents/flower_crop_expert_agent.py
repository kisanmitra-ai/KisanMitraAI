"""
KisanMitraAI Flower Crop Expert Agent
"""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class FlowerExpertRequest:
    crop: str
    crop_stage: Optional[str] = None
    location: Optional[str] = None
    season: Optional[str] = None


@dataclass
class FlowerExpertResult:
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


class FlowerCropExpertAgent:
    def __init__(self):
        self.flower_profiles: Dict[str, Dict] = {
            "rose": {
                "diseases": ["Powdery Mildew", "Black Spot", "Dieback"],
                "pests": ["Aphids", "Thrips", "Mites"],
                "nutrition": ["Potassium", "Calcium", "Organic matter"],
                "irrigation": ["Maintain consistent moisture", "Avoid leaf wetting"],
            },
            "marigold": {
                "diseases": ["Leaf Spot", "Powdery Mildew", "Root Rot"],
                "pests": ["Aphids", "Thrips", "Red Spider Mite"],
                "nutrition": ["Phosphorus", "Potassium", "Organic matter"],
                "irrigation": ["Avoid waterlogging", "Maintain moderate moisture"],
            },
            "jasmine": {
                "diseases": ["Rust", "Leaf Spot", "Wilt"],
                "pests": ["Bud Worm", "Mites", "Aphids"],
                "nutrition": ["Nitrogen balance", "Potassium", "Organic manure"],
                "irrigation": ["Regular irrigation during flowering"],
            },
            "tuberose": {
                "diseases": ["Stem Rot", "Leaf Spot", "Root Rot"],
                "pests": ["Thrips", "Aphids", "Nematodes"],
                "nutrition": ["Phosphorus", "Potassium", "Calcium"],
                "irrigation": ["Uniform moisture during spike development"],
            },
            "gerbera": {
                "diseases": ["Powdery Mildew", "Botrytis", "Root Rot"],
                "pests": ["Whitefly", "Thrips", "Mites"],
                "nutrition": ["Calcium", "Potassium", "Micronutrients"],
                "irrigation": ["Avoid overwatering", "Prefer controlled irrigation"],
            },
            "chrysanthemum": {
                "diseases": ["Rust", "Leaf Spot", "Wilt"],
                "pests": ["Aphids", "Thrips", "Leaf Miner"],
                "nutrition": ["Nitrogen balance", "Potassium", "Phosphorus"],
                "irrigation": ["Maintain soil moisture, avoid waterlogging"],
            },
            "gladiolus": {
                "diseases": ["Corm Rot", "Fusarium Wilt", "Leaf Blight"],
                "pests": ["Thrips", "Aphids", "Nematodes"],
                "nutrition": ["Phosphorus", "Potassium", "Calcium"],
                "irrigation": ["Moisture needed during spike emergence and flowering"],
            },
        }

    def advise(self, request: FlowerExpertRequest) -> FlowerExpertResult:
        crop_key = request.crop.strip().lower()
        profile = self.flower_profiles.get(crop_key)

        if not profile:
            return FlowerExpertResult(
                crop=request.crop,
                matched=False,
                crop_group="Flower",
                key_diseases=[],
                key_pests=[],
                nutrition_focus=[],
                irrigation_focus=[],
                stage_advice=["Flower crop not yet available in expert profile."],
                next_agents=["crop_expert_router_agent"],
                safety_notes=["Do not provide crop-specific fertilizer or spray advice until crop is matched."],
            )

        stage = (request.crop_stage or "general").lower()

        stage_advice = [
            f"Use {request.crop.title()} flower crop expert guidance.",
            "Flower crops need quality-focused nutrition, pest monitoring and harvest timing.",
        ]

        if "bud" in stage or "flower" in stage:
            stage_advice.append("Bud/flowering stage needs thrips/aphid monitoring and moisture stability.")
        elif "harvest" in stage:
            stage_advice.append("Harvest stage needs flower opening stage, grading and cold-chain awareness.")
        elif "vegetative" in stage:
            stage_advice.append("Vegetative stage needs healthy canopy, root health and balanced nutrition.")

        return FlowerExpertResult(
            crop=request.crop,
            matched=True,
            crop_group="Flower",
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
    agent = FlowerCropExpertAgent()
    result = agent.advise(
        FlowerExpertRequest(
            crop="Rose",
            crop_stage="Flowering",
            location="Nadia, West Bengal",
            season="Winter",
        )
    )
    print(result)
