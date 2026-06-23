from dataclasses import dataclass
from typing import List


@dataclass
class PestDetectionRequest:
    crop_name: str
    crop_stage: str
    location: str
    visible_signs: List[str]


@dataclass
class PestDetectionResult:
    crop_name: str
    probable_pest: str
    confidence: str
    risk_level: str
    possible_damage: List[str]
    recommended_next_step: str
    safety_notes: List[str]


class PestDetectionAgent:

    def analyze(self, request: PestDetectionRequest):
        pest = "Unknown Pest"
        confidence = "Low"

        signs = " ".join(request.visible_signs).lower()

        if "white insect" in signs or "sticky leaf" in signs:
            pest = "Whitefly"
            confidence = "High"

        if "hole" in signs or "fruit damage" in signs:
            pest = "Fruit Borer"
            confidence = "High"

        if "curling" in signs or "small insects" in signs:
            pest = "Aphids or Thrips"
            confidence = "Medium"

        return PestDetectionResult(
            crop_name=request.crop_name,
            probable_pest=pest,
            confidence=confidence,
            risk_level="Medium",
            possible_damage=[
                "Leaf damage",
                "Fruit damage",
                "Yield loss",
                "Disease spread risk",
            ],
            recommended_next_step="Upload clear close-up image and confirm with crop expert.",
            safety_notes=[
                "Pest detection is advisory only.",
                "Chemical recommendations require safety review.",
                "Use image evidence before farmer-facing decision.",
            ],
        )


if __name__ == "__main__":
    agent = PestDetectionAgent()
    result = agent.analyze(
        PestDetectionRequest(
            crop_name="Tomato",
            crop_stage="Flowering",
            location="Nadia, West Bengal",
            visible_signs=["white insect", "sticky leaf", "small insects"]
        )
    )
    print(result)
