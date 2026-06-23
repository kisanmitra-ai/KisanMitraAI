"""
KisanMitraAI Quality Grading Agent

Handles crop quality grading before mandi pricing or buyer matching.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class QualityGradingRequest:
    crop: str
    variety: Optional[str] = None
    image_path: Optional[str] = None
    quality_description: Optional[str] = None
    quantity_kg: Optional[float] = None


@dataclass
class QualityGradingResult:
    crop: str
    grade: str
    confidence: str
    strengths: List[str]
    defects: List[str]
    price_impact: str
    recommended_route: str
    next_actions: List[str]


class QualityGradingAgent:
    def grade(self, request: QualityGradingRequest) -> QualityGradingResult:
        if not request.image_path and not request.quality_description:
            return QualityGradingResult(
                crop=request.crop,
                grade="unknown",
                confidence="low",
                strengths=[],
                defects=["No image or quality description provided."],
                price_impact="Cannot estimate price impact without quality input.",
                recommended_route="Upload crop images or provide visible quality details.",
                next_actions=[
                    "Upload 3-5 clear images of the produce lot.",
                    "Include close-up images showing size, color, damage, moisture and defects.",
                    "Add variety, quantity and harvest date if available.",
                ],
            )

        strengths = []
        defects = []

        if request.quality_description:
            text = request.quality_description.lower()

            if any(x in text for x in ["fresh", "uniform", "good color", "clean", "large"]):
                strengths.append("Visible quality indicators suggest a better grade.")

            if any(x in text for x in ["damaged", "rotten", "crack", "spot", "small", "mixed", "wet"]):
                defects.append("Quality description mentions possible defects.")

        grade = "B"
        confidence = "medium"

        if strengths and not defects:
            grade = "A"
            confidence = "medium"
        elif defects and not strengths:
            grade = "C"
            confidence = "medium"

        price_impact = {
            "A": "May qualify for premium buyers or better mandi price.",
            "B": "Suitable for standard mandi or regular buyer sale.",
            "C": "May receive lower price; consider processing buyers or quick sale.",
        }.get(grade, "Price impact unknown.")

        recommended_route = {
            "A": "Route to premium buyer, exporter, retailer or high-quality mandi.",
            "B": "Route to verified mandi or standard buyer.",
            "C": "Route to nearby mandi, processor or fast liquidation buyer.",
        }.get(grade, "Need more quality information.")

        return QualityGradingResult(
            crop=request.crop,
            grade=grade,
            confidence=confidence,
            strengths=strengths,
            defects=defects,
            price_impact=price_impact,
            recommended_route=recommended_route,
            next_actions=[
                "Use this grade before running Best Mandi Engine.",
                "Split premium and lower-quality lots if mixed quality is present.",
                "Upload images for model-based grading when image pipeline is connected.",
            ],
        )


if __name__ == "__main__":
    agent = QualityGradingAgent()
    result = agent.grade(
        QualityGradingRequest(
            crop="Tomato",
            variety="Local",
            quality_description="Fresh tomato, good color, mostly uniform size",
            quantity_kg=1000,
        )
    )
    print(result)
