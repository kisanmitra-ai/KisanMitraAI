from dataclasses import dataclass
from typing import List


@dataclass
class DiseaseDetectionRequest:
    crop_name: str
    crop_stage: str
    location: str
    visible_symptoms: List[str]


@dataclass
class DiseaseDetectionResult:
    crop_name: str
    probable_disease: str
    confidence: str
    risk_level: str
    possible_causes: List[str]
    recommended_next_step: str
    safety_notes: List[str]


class DiseaseDetectionAgent:

    def analyze(self, request: DiseaseDetectionRequest):

        disease = "Unknown Disease"
        confidence = "Low"

        symptoms = " ".join(request.visible_symptoms).lower()

        if "yellow" in symptoms:
            disease = "Possible Nutrient Deficiency"
            confidence = "Medium"

        if "brown spot" in symptoms:
            disease = "Early Blight"
            confidence = "High"

        if "wilting" in symptoms:
            disease = "Bacterial Wilt"
            confidence = "Medium"

        return DiseaseDetectionResult(
            crop_name=request.crop_name,
            probable_disease=disease,
            confidence=confidence,
            risk_level="Medium",
            possible_causes=[
                "Weather conditions",
                "Pathogen pressure",
                "Soil issues",
            ],
            recommended_next_step=
            "Confirm with crop image and expert review.",
            safety_notes=[
                "Diagnosis is advisory only.",
                "Chemical recommendations require safety review.",
                "Use image evidence before farmer-facing decision.",
            ],
        )


if __name__ == "__main__":

    agent = DiseaseDetectionAgent()

    result = agent.analyze(
        DiseaseDetectionRequest(
            crop_name="Tomato",
            crop_stage="Flowering",
            location="Nadia, West Bengal",
            visible_symptoms=[
                "brown spot",
                "yellow leaves"
            ]
        )
    )

    print(result)