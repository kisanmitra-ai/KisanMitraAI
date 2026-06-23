from dataclasses import dataclass
from typing import List


@dataclass
class PlantStressRequest:
    crop_name: str
    crop_stage: str
    location: str
    visible_symptoms: List[str]
    temperature_c: float = 0
    humidity_percent: float = 0
    soil_moisture_status: str = "unknown"


@dataclass
class PlantStressResult:
    crop_name: str
    probable_stress: str
    confidence: str
    risk_level: str
    possible_causes: List[str]
    recommended_next_step: str
    safety_notes: List[str]


class PlantStressAgent:

    def analyze(self, request: PlantStressRequest):
        stress = "Unknown Stress"
        confidence = "Low"
        risk = "Medium"

        symptoms = " ".join(request.visible_symptoms).lower()

        if "yellow" in symptoms or "pale" in symptoms:
            stress = "Possible Nitrogen Deficiency"
            confidence = "Medium"

        if "leaf edge burn" in symptoms or "scorching" in symptoms:
            stress = "Possible Potassium Deficiency or Heat Stress"
            confidence = "Medium"

        if "wilting" in symptoms or request.soil_moisture_status.lower() == "dry":
            stress = "Water Stress"
            confidence = "High"
            risk = "High"

        if request.temperature_c >= 35:
            stress = "Heat Stress"
            confidence = "High"
            risk = "High"

        if "waterlogging" in symptoms or "root rot" in symptoms:
            stress = "Flood / Waterlogging Stress"
            confidence = "High"
            risk = "High"

        return PlantStressResult(
            crop_name=request.crop_name,
            probable_stress=stress,
            confidence=confidence,
            risk_level=risk,
            possible_causes=[
                "Soil moisture imbalance",
                "Nutrient deficiency",
                "High temperature",
                "Poor drainage",
                "Crop-stage stress",
            ],
            recommended_next_step="Confirm with soil moisture, weather, crop stage and image evidence.",
            safety_notes=[
                "Stress detection is advisory only.",
                "Fertilizer recommendation requires soil test or expert validation.",
                "Use crop expert and weather intelligence before farmer-facing action.",
            ],
        )


if __name__ == "__main__":
    agent = PlantStressAgent()
    result = agent.analyze(
        PlantStressRequest(
            crop_name="Tomato",
            crop_stage="Flowering",
            location="Nadia, West Bengal",
            visible_symptoms=["wilting", "yellow leaves"],
            temperature_c=36,
            humidity_percent=60,
            soil_moisture_status="dry",
        )
    )
    print(result)
