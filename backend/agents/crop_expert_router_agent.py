"""
KisanMitraAI Crop Expert Router Agent

Purpose:
- Route crop scan / crop planning requests to the correct crop expert knowledge profile
- Avoid creating hundreds of separate crop expert files
- Use crop registry style logic for scalable crop intelligence

MVP:
This uses internal crop profiles.
Later, move crop profiles to backend/data/crop_registry.json.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class CropExpertRequest:
    crop_name: str
    location: Optional[str] = None
    crop_stage: Optional[str] = None
    season: Optional[str] = None


@dataclass
class CropExpertResult:
    crop_name: str
    matched_crop: str
    confidence: str
    expert_group: str
    common_diseases: List[str]
    common_pests: List[str]
    key_stress_risks: List[str]
    planning_focus: List[str]
    next_agents: List[str]
    safety_notes: List[str]


class CropExpertRouterAgent:

    def __init__(self):
        self.crop_profiles: Dict[str, Dict] = {
            "tomato": {
                "expert_group": "Vegetable Crop Expert",
                "common_diseases": ["Early Blight", "Late Blight", "Bacterial Spot", "Leaf Curl Virus"],
                "common_pests": ["Whitefly", "Fruit Borer", "Aphids", "Thrips"],
                "key_stress_risks": ["Heat stress", "Water stress", "Nutrient imbalance"],
                "planning_focus": ["Nursery health", "Transplanting", "Flowering nutrition", "Fruit protection"],
            },
            "potato": {
                "expert_group": "Vegetable Crop Expert",
                "common_diseases": ["Late Blight", "Early Blight", "Black Scurf"],
                "common_pests": ["Aphids", "Cutworm", "Tuber Moth"],
                "key_stress_risks": ["Waterlogging", "Low temperature stress", "Nutrient deficiency"],
                "planning_focus": ["Seed tuber quality", "Ridge preparation", "Blight prevention", "Harvest timing"],
            },
            "rice": {
                "expert_group": "Cereal Crop Expert",
                "common_diseases": ["Blast", "Sheath Blight", "Bacterial Leaf Blight"],
                "common_pests": ["Stem Borer", "Brown Planthopper", "Leaf Folder"],
                "key_stress_risks": ["Flood stress", "Drought stress", "Nitrogen imbalance"],
                "planning_focus": ["Nursery", "Transplanting", "Water control", "Panicle stage protection"],
            },
            "wheat": {
                "expert_group": "Cereal Crop Expert",
                "common_diseases": ["Rust", "Powdery Mildew", "Karnal Bunt"],
                "common_pests": ["Aphids", "Termites"],
                "key_stress_risks": ["Heat stress", "Water stress", "Nutrient deficiency"],
                "planning_focus": ["Sowing window", "Irrigation stages", "Rust monitoring", "Harvest timing"],
            },
            "banana": {
                "expert_group": "Fruit Crop Expert",
                "common_diseases": ["Sigatoka Leaf Spot", "Panama Wilt", "Bunchy Top Virus"],
                "common_pests": ["Rhizome Weevil", "Nematodes", "Aphids"],
                "key_stress_risks": ["Wind damage", "Water stress", "Nutrient deficiency"],
                "planning_focus": ["Sucker selection", "Irrigation", "Nutrition", "Disease monitoring"],
            },
            "mango": {
                "expert_group": "Fruit Crop Expert",
                "common_diseases": ["Anthracnose", "Powdery Mildew", "Dieback"],
                "common_pests": ["Mango Hopper", "Fruit Fly", "Mealybug"],
                "key_stress_risks": ["Flower drop", "Heat stress", "Moisture stress"],
                "planning_focus": ["Flowering protection", "Fruit set", "Pest control", "Harvest quality"],
            },
            "onion": {
                "expert_group": "Vegetable Crop Expert",
                "common_diseases": ["Purple Blotch", "Downy Mildew", "Basal Rot"],
                "common_pests": ["Thrips", "Cutworm"],
                "key_stress_risks": ["Water stress", "Heat stress", "Storage rot risk"],
                "planning_focus": ["Nursery", "Bulb formation", "Thrips control", "Curing and storage"],
            },
            "chilli": {
                "expert_group": "Vegetable Crop Expert",
                "common_diseases": ["Anthracnose", "Leaf Curl Virus", "Powdery Mildew"],
                "common_pests": ["Thrips", "Mites", "Aphids"],
                "key_stress_risks": ["Heat stress", "Moisture stress", "Nutrient imbalance"],
                "planning_focus": ["Transplanting", "Flowering", "Fruit protection", "Harvest intervals"],
            },
        }

    def route(self, request: CropExpertRequest) -> CropExpertResult:
        crop_key = request.crop_name.strip().lower()

        profile = self.crop_profiles.get(crop_key)

        if profile:
            matched_crop = crop_key.title()
            confidence = "high"
        else:
            matched_crop = "Unknown crop"
            confidence = "low"
            profile = {
                "expert_group": "General Crop Expert",
                "common_diseases": [],
                "common_pests": [],
                "key_stress_risks": ["Weather stress", "Water stress", "Nutrient stress"],
                "planning_focus": ["Identify crop", "Confirm crop stage", "Collect location and photos"],
            }

        next_agents = [
            "weather_intelligence_agent",
            "disease_detection_agent",
            "pest_detection_agent",
            "plant_stress_agent",
            "crop_planning_agent",
            "crop_passport_agent",
            "crop_knowledge_graph_agent",
            "farmer_recommendation_agent",`n            "crop_knowledge_graph_agent",`n            "farmer_recommendation_agent",
        ]

        safety_notes = [
            "Crop expert routing is advisory and must be confirmed when confidence is low.",
            "Disease, pest and spray advice must pass safety review before farmer-facing chemical recommendation.",
            "Use location, crop stage, weather and image evidence before final action plan.",
        ]

        return CropExpertResult(
            crop_name=request.crop_name,
            matched_crop=matched_crop,
            confidence=confidence,
            expert_group=profile["expert_group"],
            common_diseases=profile["common_diseases"],
            common_pests=profile["common_pests"],
            key_stress_risks=profile["key_stress_risks"],
            planning_focus=profile["planning_focus"],
            next_agents=next_agents,
            safety_notes=safety_notes,
        )


if __name__ == "__main__":
    agent = CropExpertRouterAgent()

    result = agent.route(
        CropExpertRequest(
            crop_name="Tomato",
            location="Nadia, West Bengal",
            crop_stage="Flowering",
            season="Kharif",
        )
    )

    print(result)


