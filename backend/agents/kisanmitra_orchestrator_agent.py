"""
KisanMitraAI Main Orchestrator Agent

Routes farmer, FPO, buyer and institutional requests to the correct internal agent.
This is the top-level decision layer for KisanMitraAI.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class AgentRoute:
    primary_agent: str
    secondary_agents: List[str]
    reason: str
    required_missing_fields: List[str]


class KisanMitraOrchestratorAgent:
    def __init__(self):
        self.agent_map = {
            "best_mandi": "BEST_MANDI_ENGINE",
            "deal_os": "DEAL_OS_ENGINE",
            "quality_grading": "QUALITY_GRADING_ENGINE",
            "farm_intelligence": "FARM_INTELLIGENCE_ENGINE",
            "fpo_os": "FPO_OS_ENGINE",
            "trust": "TRUST_ENGINE",
        }

    def detect_intent(self, message: str) -> str:
        text = message.lower()

        if any(x in text for x in ["where to sell", "best mandi", "mandi", "best price", "net profit"]):
            return "best_mandi"

        if any(x in text for x in ["buyer", "deal", "contract", "agreement", "requirement", "connect"]):
            return "deal_os"

        if any(x in text for x in ["quality", "grade", "grading", "defect", "premium", "image", "photo"]):
            return "quality_grading"

        if any(x in text for x in ["satellite", "soil", "crop suitability", "weather", "disease", "pest", "farm"]):
            return "farm_intelligence"

        if any(x in text for x in ["fpo", "farmer records", "aggregation", "collection center", "accounts"]):
            return "fpo_os"

        if any(x in text for x in ["trust", "verification", "payment risk", "fraud", "reputation"]):
            return "trust"

        return "general"

    def required_fields_for_intent(self, intent: str) -> List[str]:
        required = {
            "best_mandi": ["crop", "quantity", "location", "time_window"],
            "deal_os": ["crop_or_requirement", "quantity", "location", "quality_expectation"],
            "quality_grading": ["crop", "image_or_quality_description"],
            "farm_intelligence": ["farm_location_or_boundary", "crop"],
            "fpo_os": ["fpo_name_or_id", "operation_type"],
            "trust": ["counterparty_name_or_id"],
        }
        return required.get(intent, [])

    def find_missing_fields(self, intent: str, context: Dict) -> List[str]:
        required = self.required_fields_for_intent(intent)
        return [field for field in required if not context.get(field)]

    def route(self, message: str, context: Optional[Dict] = None) -> AgentRoute:
        context = context or {}
        intent = self.detect_intent(message)
        missing = self.find_missing_fields(intent, context)

        if intent == "quality_grading":
            return AgentRoute(
                primary_agent="QUALITY_GRADING_ENGINE",
                secondary_agents=["BEST_MANDI_ENGINE", "DEAL_OS_ENGINE"],
                reason="Quality must be understood before price or buyer matching.",
                required_missing_fields=missing,
            )

        if intent == "best_mandi":
            return AgentRoute(
                primary_agent="BEST_MANDI_ENGINE",
                secondary_agents=["DEAL_OS_ENGINE"],
                reason="The user is asking for best selling option or net price.",
                required_missing_fields=missing,
            )

        if intent == "deal_os":
            return AgentRoute(
                primary_agent="DEAL_OS_ENGINE",
                secondary_agents=["TRUST_ENGINE"],
                reason="The user is asking for buyer matching, deal structure or contract flow.",
                required_missing_fields=missing,
            )

        if intent == "farm_intelligence":
            return AgentRoute(
                primary_agent="FARM_INTELLIGENCE_ENGINE",
                secondary_agents=["QUALITY_GRADING_ENGINE", "BEST_MANDI_ENGINE"],
                reason="The user is asking about farm, crop, soil, satellite, weather or risk intelligence.",
                required_missing_fields=missing,
            )

        if intent == "fpo_os":
            return AgentRoute(
                primary_agent="FPO_OS_ENGINE",
                secondary_agents=["DEAL_OS_ENGINE", "TRUST_ENGINE"],
                reason="The user is asking about FPO operations or farmer management.",
                required_missing_fields=missing,
            )

        if intent == "trust":
            return AgentRoute(
                primary_agent="TRUST_ENGINE",
                secondary_agents=["DEAL_OS_ENGINE"],
                reason="The user is asking about trust, verification or payment risk.",
                required_missing_fields=missing,
            )

        return AgentRoute(
            primary_agent="GENERAL_KISANMITRA_ASSISTANT",
            secondary_agents=[],
            reason="No specific engine was required. General agricultural guidance can be provided.",
            required_missing_fields=[],
        )

    def format_response_shell(self, route: AgentRoute) -> Dict:
        return {
            "summary": "",
            "details": {
                "primary_agent": route.primary_agent,
                "secondary_agents": route.secondary_agents,
                "reason": route.reason,
                "missing_fields": route.required_missing_fields,
            },
            "next_actions": [],
        }


if __name__ == "__main__":
    agent = KisanMitraOrchestratorAgent()
    result = agent.route(
        "Where should I sell 1000 kg tomato near Nadia?",
        {
            "crop": "tomato",
            "quantity": "1000 kg",
            "location": "Nadia, West Bengal",
        },
    )
    print(result)
