from dataclasses import dataclass
from typing import List


@dataclass
class CropVisionScanRequest:
    image_path: str
    location: str = ""
    crop_stage: str = ""


@dataclass
class CropVisionScanResult:
    detected_crop: str
    confidence: str
    possible_diseases: List[str]
    possible_pests: List[str]
    nutrient_deficiencies: List[str]
    stress_signals: List[str]
    next_agents: List[str]
    safety_notes: List[str]


class CropVisionScanAgent:

    def analyze(self, request: CropVisionScanRequest):

        return CropVisionScanResult(
            detected_crop="Unknown",
            confidence="Low",
            possible_diseases=[],
            possible_pests=[],
            nutrient_deficiencies=[],
            stress_signals=[],
            next_agents=[
                "crop_expert_router_agent",
                "disease_detection_agent",
                "pest_detection_agent",
                "plant_stress_agent",
                "farmer_recommendation_agent",
            ],
            safety_notes=[
                "Vision result is advisory only.",
                "Use image evidence plus crop expert validation.",
                "Chemical recommendation requires safety review.",
            ],
        )


if __name__ == "__main__":

    agent = CropVisionScanAgent()

    result = agent.analyze(
        CropVisionScanRequest(
            image_path="sample_crop.jpg",
            location="Nadia, West Bengal",
            crop_stage="Flowering",
        )
    )

    print(result)