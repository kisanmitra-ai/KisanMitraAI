"""
KisanMitraAI Pulse Crop Expert Agent
"""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class PulseExpertRequest:
    crop: str
    crop_stage: Optional[str] = None
    location: Optional[str] = None
    season: Optional[str] = None


@dataclass
class PulseExpertResult:
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


class PulseCropExpertAgent:
    def __init__(self):
        self.pulse_profiles: Dict[str, Dict] = {
            "moong": {
                "diseases": ["Yellow Mosaic Virus", "Powdery Mildew", "Cercospora Leaf Spot"],
                "pests": ["Whitefly", "Aphids", "Pod Borer"],
                "nutrition": ["Rhizobium inoculation", "Phosphorus", "Sulphur", "Organic matter"],
                "irrigation": ["Avoid waterlogging", "Light irrigation during flowering and pod formation"],
            },
            "urad": {
                "diseases": ["Yellow Mosaic Virus", "Leaf Spot", "Root Rot"],
                "pests": ["Whitefly", "Aphids", "Pod Borer"],
                "nutrition": ["Rhizobium inoculation", "Phosphorus", "Sulphur"],
                "irrigation": ["Avoid excess water", "Maintain moisture during flowering"],
            },
            "arhar": {
                "diseases": ["Fusarium Wilt", "Sterility Mosaic Disease", "Phytophthora Blight"],
                "pests": ["Pod Borer", "Maruca Pod Borer", "Aphids"],
                "nutrition": ["Phosphorus", "Sulphur", "Rhizobium", "Organic matter"],
                "irrigation": ["Avoid waterlogging", "Critical moisture during flowering and pod filling"],
            },
            "gram": {
                "diseases": ["Fusarium Wilt", "Ascochyta Blight", "Root Rot"],
                "pests": ["Gram Pod Borer", "Cutworm", "Aphids"],
                "nutrition": ["Rhizobium inoculation", "Phosphorus", "Sulphur"],
                "irrigation": ["Usually low water need, avoid excess irrigation"],
            },
            "lentil": {
                "diseases": ["Wilt", "Rust", "Stemphylium Blight"],
                "pests": ["Aphids", "Pod Borer"],
                "nutrition": ["Rhizobium", "Phosphorus", "Sulphur"],
                "irrigation": ["Avoid standing water, light irrigation if moisture stress appears"],
            },
        }

    def advise(self, request: PulseExpertRequest) -> PulseExpertResult:
        crop_key = request.crop.strip().lower()
        profile = self.pulse_profiles.get(crop_key)

        if not profile:
            return PulseExpertResult(
                crop=request.crop,
                matched=False,
                crop_group="Pulse",
                key_diseases=[],
                key_pests=[],
                nutrition_focus=[],
                irrigation_focus=[],
                stage_advice=["Pulse crop not yet available in expert profile."],
                next_agents=["crop_expert_router_agent"],
                safety_notes=["Do not provide crop-specific fertilizer or spray advice until crop is matched."],
            )

        stage = (request.crop_stage or "general").lower()

        stage_advice = [
            f"Use {request.crop.title()} pulse crop expert guidance.",
            "Protect root health and avoid waterlogging because pulses are sensitive to excess moisture.",
            "Use Rhizobium/seed treatment guidance only after local validation.",
        ]

        if "flower" in stage:
            stage_advice.append("Flowering stage needs moisture stability and close pod borer monitoring.")
        elif "pod" in stage:
            stage_advice.append("Pod formation stage needs pest scouting and moisture protection.")
        elif "harvest" in stage:
            stage_advice.append("Harvest stage needs grain maturity check and dry-weather planning.")

        return PulseExpertResult(
            crop=request.crop,
            matched=True,
            crop_group="Pulse",
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
    agent = PulseCropExpertAgent()
    result = agent.advise(
        PulseExpertRequest(
            crop="Moong",
            crop_stage="Flowering",
            location="Nadia, West Bengal",
            season="Kharif",
        )
    )
    print(result)
