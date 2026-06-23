"""
KisanMitraAI Main Orchestrator Agent

Routes farmer, FPO, buyer and institutional requests to the correct internal agents.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional

from farm_intelligence_agent import FarmIntelligenceAgent, FarmIntelligenceRequest
from quality_grading_agent import QualityGradingAgent, QualityGradingRequest
from best_mandi_agent import BestMandiAgent, BestMandiRequest
from deal_os_agent import DealOSAgent, DealRequest
from trust_agent import TrustAgent, TrustRequest
from fpo_os_agent import FPOOSAgent, FPORequest


@dataclass
class AgentRoute:
    primary_agent: str
    secondary_agents: List[str]
    reason: str
    required_missing_fields: List[str]


class KisanMitraOrchestratorAgent:

    def __init__(self):
        self.farm_agent = FarmIntelligenceAgent()
        self.quality_agent = QualityGradingAgent()
        self.mandi_agent = BestMandiAgent()
        self.deal_agent = DealOSAgent()
        self.trust_agent = TrustAgent()
        self.fpo_agent = FPOOSAgent()

    def detect_intent(self, message: str) -> str:
        text = message.lower()

        if any(x in text for x in ["quality", "grade", "grading", "defect", "premium", "image", "photo"]):
            return "quality_grading"

        if any(x in text for x in ["where to sell", "sell", "selling", "best mandi", "mandi", "best price", "net profit"]):
            return "best_mandi"

        if any(x in text for x in ["buyer", "deal", "contract", "agreement", "requirement", "connect"]):
            return "deal_os"

        if any(x in text for x in ["satellite", "soil", "crop suitability", "weather", "disease", "pest", "farm"]):
            return "farm_intelligence"

        if any(x in text for x in ["fpo", "farmer records", "aggregation", "collection center", "accounts"]):
            return "fpo_os"

        if any(x in text for x in ["trust", "verification", "payment risk", "fraud", "reputation"]):
            return "trust"

        return "general"

    def route(self, message: str, context: Optional[Dict] = None) -> AgentRoute:
        context = context or {}
        intent = self.detect_intent(message)

        missing = []

        required = {
            "quality_grading": ["crop"],
            "best_mandi": ["crop", "quantity_kg", "location"],
            "deal_os": ["crop", "quantity_kg", "location"],
            "farm_intelligence": ["location"],
            "fpo_os": ["fpo_name", "operation_type"],
            "trust": ["counterparty_name"],
        }.get(intent, [])

        for field in required:
            if not context.get(field):
                missing.append(field)

        engine_map = {
            "quality_grading": ("QUALITY_GRADING_ENGINE", ["BEST_MANDI_ENGINE", "DEAL_OS_ENGINE"]),
            "best_mandi": ("BEST_MANDI_ENGINE", ["DEAL_OS_ENGINE"]),
            "deal_os": ("DEAL_OS_ENGINE", ["TRUST_ENGINE"]),
            "farm_intelligence": ("FARM_INTELLIGENCE_ENGINE", ["QUALITY_GRADING_ENGINE", "BEST_MANDI_ENGINE"]),
            "fpo_os": ("FPO_OS_ENGINE", ["DEAL_OS_ENGINE", "TRUST_ENGINE"]),
            "trust": ("TRUST_ENGINE", ["DEAL_OS_ENGINE"]),
            "general": ("GENERAL_KISANMITRA_ASSISTANT", []),
        }

        primary, secondary = engine_map[intent]

        return AgentRoute(
            primary_agent=primary,
            secondary_agents=secondary,
            reason=f"Detected intent: {intent}",
            required_missing_fields=missing,
        )

    def run_workflow(self, message: str, context: Optional[Dict] = None) -> Dict:
        context = context or {}
        route = self.route(message, context)

        if route.required_missing_fields:
            return {
                "summary": "More information is needed before running the full recommendation.",
                "details": {
                    "route": route,
                    "missing_fields": route.required_missing_fields,
                },
                "next_actions": [
                    f"Please provide: {', '.join(route.required_missing_fields)}"
                ],
            }

        outputs = {}

        if route.primary_agent == "FARM_INTELLIGENCE_ENGINE":
            outputs["farm_intelligence"] = self.farm_agent.analyze(
                FarmIntelligenceRequest(
                    farm_location=context.get("location"),
                    crop=context.get("crop"),
                    area_acres=context.get("area_acres"),
                )
            )

        if route.primary_agent == "QUALITY_GRADING_ENGINE":
            outputs["quality_grading"] = self.quality_agent.grade(
                QualityGradingRequest(
                    crop=context.get("crop"),
                    variety=context.get("variety"),
                    image_path=context.get("image_path"),
                    quality_description=context.get("quality_description"),
                    quantity_kg=context.get("quantity_kg"),
                )
            )

        if route.primary_agent == "BEST_MANDI_ENGINE":
            outputs["best_mandi"] = self.mandi_agent.evaluate(
                BestMandiRequest(
                    crop=context.get("crop"),
                    quantity_kg=context.get("quantity_kg"),
                    location=context.get("location"),
                    time_window=context.get("time_window", "today"),
                )
            )

            outputs["deal_os"] = self.deal_agent.match(
                DealRequest(
                    crop=context.get("crop"),
                    quantity_kg=context.get("quantity_kg"),
                    location=context.get("location"),
                    quality_grade=context.get("quality_grade", "B"),
                    expected_price_per_kg=outputs["best_mandi"].best_option.net_price_per_kg,
                )
            )

        if route.primary_agent == "DEAL_OS_ENGINE":
            outputs["deal_os"] = self.deal_agent.match(
                DealRequest(
                    crop=context.get("crop"),
                    quantity_kg=context.get("quantity_kg"),
                    location=context.get("location"),
                    quality_grade=context.get("quality_grade", "B"),
                    expected_price_per_kg=context.get("expected_price_per_kg"),
                )
            )

        if route.primary_agent == "TRUST_ENGINE":
            outputs["trust"] = self.trust_agent.evaluate(
                TrustRequest(
                    counterparty_name=context.get("counterparty_name"),
                    counterparty_type=context.get("counterparty_type", "Buyer"),
                    location=context.get("location", "Unknown"),
                    deal_value=context.get("deal_value", 0),
                    previous_deals_count=context.get("previous_deals_count", 0),
                    on_time_payment_rate=context.get("on_time_payment_rate", 0),
                    dispute_count=context.get("dispute_count", 0),
                    verified=context.get("verified", False),
                )
            )

        if route.primary_agent == "FPO_OS_ENGINE":
            outputs["fpo_os"] = self.fpo_agent.manage(
                FPORequest(
                    fpo_name=context.get("fpo_name"),
                    operation_type=context.get("operation_type"),
                    crop=context.get("crop"),
                    location=context.get("location"),
                )
            )

        return {
            "summary": "KisanMitraAI agent workflow completed.",
            "details": outputs,
            "next_actions": [
                "Review the recommendation.",
                "Confirm quantity, quality and location.",
                "Proceed to deal creation if suitable.",
            ],
        }


if __name__ == "__main__":
    agent = KisanMitraOrchestratorAgent()

    result = agent.run_workflow(
        "Where should I sell 1000 kg tomato near Nadia?",
        {
            "crop": "Tomato",
            "quantity_kg": 1000,
            "location": "Nadia, West Bengal",
            "time_window": "today",
            "quality_grade": "A",
        },
    )

    print(result)
