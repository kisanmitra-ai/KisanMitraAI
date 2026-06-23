from dataclasses import dataclass
from typing import Dict, List


@dataclass
class CropDoctorWorkflowRequest:
    crop_name: str
    crop_stage: str
    location: str
    image_path: str = ""


@dataclass
class CropDoctorWorkflowResult:
    crop_name: str
    crop_stage: str
    location: str
    workflow_steps: List[str]
    diagnosis_summary: Dict[str, str]
    farmer_recommendation: List[str]
    passport_update: List[str]
    safety_notes: List[str]


class CropDoctorWorkflowAgent:

    def run(self, request: CropDoctorWorkflowRequest) -> CropDoctorWorkflowResult:
        workflow_steps = [
            "Run crop vision scan",
            "Route to crop expert",
            "Run disease detection",
            "Run pest detection",
            "Run plant stress detection",
            "Check weather intelligence",
            "Generate farmer recommendation",
            "Update crop passport",
        ]

        diagnosis_summary = {
            "crop": request.crop_name,
            "stage": request.crop_stage,
            "disease_risk": "Medium",
            "pest_risk": "Medium",
            "stress_risk": "Medium",
            "weather_risk": "Check live weather provider",
        }

        return CropDoctorWorkflowResult(
            crop_name=request.crop_name,
            crop_stage=request.crop_stage,
            location=request.location,
            workflow_steps=workflow_steps,
            diagnosis_summary=diagnosis_summary,
            farmer_recommendation=[
                "Inspect crop closely and upload clear leaf/plant images.",
                "Avoid chemical spray until expert/admin safety review.",
                "Check soil moisture before irrigation.",
                "Update crop passport with scan evidence.",
            ],
            passport_update=[
                "Add scan event",
                "Add diagnosis summary",
                "Add weather context",
                "Add farmer recommendation",
            ],
            safety_notes=[
                "This workflow is advisory only.",
                "Chemical treatment must pass safety review.",
                "Use crop expert, image evidence and weather context before farmer-facing action.",
            ],
        )


if __name__ == "__main__":
    agent = CropDoctorWorkflowAgent()
    result = agent.run(
        CropDoctorWorkflowRequest(
            crop_name="Tomato",
            crop_stage="Flowering",
            location="Nadia, West Bengal",
            image_path="sample_crop.jpg",
        )
    )
    print(result)