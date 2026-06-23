from dataclasses import dataclass
from typing import List


@dataclass
class FarmerRecommendationRequest:
    crop_name: str
    crop_stage: str
    location: str
    disease_risk: str
    pest_risk: str
    stress_risk: str
    weather_alert: str


@dataclass
class FarmerRecommendationResult:
    crop_name: str
    crop_stage: str
    priority: str
    summary: str
    todays_tasks: List[str]
    avoid_actions: List[str]
    next_actions: List[str]
    safety_notes: List[str]


class FarmerRecommendationAgent:

    def generate(self, request: FarmerRecommendationRequest):
        priority = "Medium"

        if "high" in request.disease_risk.lower() or "high" in request.stress_risk.lower():
            priority = "High"

        todays_tasks = [
            "Inspect crop leaves and stems carefully.",
            "Take 2-3 clear photos for evidence.",
            "Check soil moisture before irrigation.",
        ]

        avoid_actions = [
            "Do not spray chemicals without safety review.",
        ]

        if "rain" in request.weather_alert.lower():
            avoid_actions.append("Avoid spraying before rain.")

        next_actions = [
            "Run crop vision scan.",
            "Update crop passport.",
            "Check tomorrow's weather.",
            "Review crop expert advice.",
        ]

        return FarmerRecommendationResult(
            crop_name=request.crop_name,
            crop_stage=request.crop_stage,
            priority=priority,
            summary=f"{request.crop_name} at {request.crop_stage} stage needs attention. Disease: {request.disease_risk}, Pest: {request.pest_risk}, Stress: {request.stress_risk}.",
            todays_tasks=todays_tasks,
            avoid_actions=avoid_actions,
            next_actions=next_actions,
            safety_notes=[
                "This is advisory guidance only.",
                "Chemical treatment must pass expert/admin safety review.",
                "Use soil test and image evidence before final action.",
            ],
        )


if __name__ == "__main__":
    agent = FarmerRecommendationAgent()
    result = agent.generate(
        FarmerRecommendationRequest(
            crop_name="Tomato",
            crop_stage="Flowering",
            location="Nadia, West Bengal",
            disease_risk="Medium",
            pest_risk="Medium",
            stress_risk="High",
            weather_alert="Rain expected within 24 hours",
        )
    )
    print(result)
