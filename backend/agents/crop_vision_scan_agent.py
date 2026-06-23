"""
KisanMitraAI Crop Vision Scan Agent

Purpose:
- Scan live camera or uploaded crop/leaf image
- Recognize possible crop/plant
- Detect visible disease, pest, stress or nutrient symptoms
- Combine with GPS + weather + rain risk
- Return farmer-friendly advisory with safety warnings

Important:
This is MVP logic. Real vision model integration must be added later.
Never claim exact disease diagnosis without confidence and expert/lab validation.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class CropVisionScanRequest:
    image_path: Optional[str]
    location: Optional[str]
    crop_hint: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    temperature_c: Optional[float] = None
    humidity_percent: Optional[float] = None
    rain_chance_percent: Optional[float] = None
    farmer_language: Optional[str] = "English"


@dataclass
class CropVisionScanResult:
    crop_detected: str
    confidence: str
    visible_condition: str
    possible_issues: List[str]
    disease_risk: str
    pest_risk: str
    plant_stress_risk: str
    weather_context: Dict
    farmer_advice: List[str]
    safety_warning: str
    next_actions: List[str]


class CropVisionScanAgent:

    def scan(self, request: CropVisionScanRequest) -> CropVisionScanResult:
        crop_detected = request.crop_hint or "Unknown plant/crop"
        confidence = "low"

        possible_issues = []
        visible_condition = "Image received. Real AI vision model is not connected yet."

        if request.crop_hint:
            confidence = "medium"

        humidity = request.humidity_percent or 0
        rain = request.rain_chance_percent or 0
        temp = request.temperature_c or 0

        disease_risk = "Unknown"
        pest_risk = "Unknown"
        plant_stress_risk = "Unknown"

        if humidity >= 75 or rain >= 50:
            disease_risk = "Medium to High"
            possible_issues.append("High humidity or rain may increase fungal/bacterial disease risk.")
        elif humidity > 0:
            disease_risk = "Low to Medium"

        if temp >= 30:
            pest_risk = "Medium"
            possible_issues.append("Warm temperature may increase pest activity.")
        elif temp > 0:
            pest_risk = "Low"

        if temp >= 35:
            plant_stress_risk = "High"
            possible_issues.append("High temperature may cause heat or water stress.")
        elif temp >= 30:
            plant_stress_risk = "Medium"
        elif temp > 0:
            plant_stress_risk = "Low"

        weather_context = {
            "location": request.location,
            "latitude": request.latitude,
            "longitude": request.longitude,
            "temperature_c": request.temperature_c,
            "humidity_percent": request.humidity_percent,
            "rain_chance_percent": request.rain_chance_percent,
        }

        farmer_advice = [
            "Take 2-3 more clear photos: one close-up leaf, one full plant, one field view.",
            "Do not spray chemicals only from image result. Wait for safer recommendation or expert review.",
            "Check whether the problem is spreading from lower leaves, upper leaves, or fruit/stem.",
            "Keep record of date, location, crop stage and recent rain.",
        ]

        if disease_risk in ["Medium to High"]:
            farmer_advice.append("Avoid overhead watering if possible and improve air movement around plants.")

        if plant_stress_risk == "High":
            farmer_advice.append("Check soil moisture and irrigate during cooler hours if crop needs water.")

        return CropVisionScanResult(
            crop_detected=crop_detected,
            confidence=confidence,
            visible_condition=visible_condition,
            possible_issues=possible_issues,
            disease_risk=disease_risk,
            pest_risk=pest_risk,
            plant_stress_risk=plant_stress_risk,
            weather_context=weather_context,
            farmer_advice=farmer_advice,
            safety_warning="This is an AI-assisted preliminary scan, not a certified diagnosis. Chemical spray advice must pass safety review.",
            next_actions=[
                "Connect real crop recognition model.",
                "Connect disease and pest image model.",
                "Connect live GPS weather provider.",
                "Add Admin Safety Gate before showing chemical treatment.",
                "Store scan history in crop image evidence timeline.",
            ],
        )


if __name__ == "__main__":
    agent = CropVisionScanAgent()

    result = agent.scan(
        CropVisionScanRequest(
            image_path="sample_leaf.jpg",
            location="Nadia, West Bengal",
            crop_hint="Tomato",
            temperature_c=34,
            humidity_percent=78,
            rain_chance_percent=55,
        )
    )

    print(result)
