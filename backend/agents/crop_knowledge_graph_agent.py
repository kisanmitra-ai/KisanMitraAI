from dataclasses import dataclass
from typing import List


@dataclass
class CropKnowledgeGraphRequest:
    crop_name: str
    crop_stage: str
    location: str


@dataclass
class CropKnowledgeGraphResult:
    crop_name: str
    crop_stage: str
    crop_group: str
    linked_agents: List[str]
    knowledge_nodes: List[str]
    next_actions: List[str]


class CropKnowledgeGraphAgent:

    def build(self, request: CropKnowledgeGraphRequest):
        crop = request.crop_name.lower()
        crop_group = "Unknown"

        if crop in ["tomato", "brinjal", "chilli", "cabbage", "potato", "onion"]:
            crop_group = "Vegetable"
        elif crop in ["rice", "wheat", "maize", "millet", "barley"]:
            crop_group = "Cereal"
        elif crop in ["mango", "banana", "guava", "papaya"]:
            crop_group = "Fruit"

        return CropKnowledgeGraphResult(
            crop_name=request.crop_name,
            crop_stage=request.crop_stage,
            crop_group=crop_group,
            linked_agents=[
                "crop_vision_scan_agent",
                "disease_detection_agent",
                "pest_detection_agent",
                "plant_stress_agent",
                "weather_intelligence_agent",
                "crop_planning_agent",
                "daily_task_engine",
                "crop_passport_agent",
                "crop_expert_router_agent",
            ],
            knowledge_nodes=[
                "Crop",
                "Crop Stage",
                "Disease",
                "Pest",
                "Stress",
                "Weather",
                "Nutrition",
                "Irrigation",
                "Tasks",
                "Passport Evidence",
            ],
            next_actions=[
                "Connect expert network.",
                "Connect real weather feed.",
                "Connect vision AI.",
                "Connect crop passport.",
                "Enable farmer recommendation engine.",
            ],
        )


if __name__ == "__main__":
    agent = CropKnowledgeGraphAgent()
    result = agent.build(
        CropKnowledgeGraphRequest(
            crop_name="Tomato",
            crop_stage="Flowering",
            location="Nadia, West Bengal",
        )
    )
    print(result)
