"""
KisanMitraAI Trust Engine

Purpose:
- Verify buyers/FPOs
- Estimate payment risk
- Estimate delivery reliability
- Recommend safe deal terms
"""

from dataclasses import dataclass
from typing import List


@dataclass
class TrustRequest:
    counterparty_name: str
    counterparty_type: str
    location: str
    deal_value: float
    previous_deals_count: int = 0
    on_time_payment_rate: float = 0.0
    dispute_count: int = 0
    verified: bool = False


@dataclass
class TrustResult:
    counterparty_name: str
    trust_score: int
    risk_level: str
    payment_recommendation: str
    advance_recommendation: str
    warnings: List[str]
    next_actions: List[str]


class TrustAgent:

    def evaluate(self, request: TrustRequest) -> TrustResult:
        score = 50
        warnings = []

        if request.verified:
            score += 20
        else:
            warnings.append("Counterparty is not fully verified.")

        if request.previous_deals_count >= 10:
            score += 15
        elif request.previous_deals_count >= 3:
            score += 8
        else:
            warnings.append("Limited past deal history.")

        if request.on_time_payment_rate >= 90:
            score += 15
        elif request.on_time_payment_rate >= 70:
            score += 8
        else:
            warnings.append("Payment reliability is not strong enough.")

        if request.dispute_count > 0:
            score -= min(request.dispute_count * 10, 25)
            warnings.append("Past dispute history found.")

        if request.deal_value > 100000:
            warnings.append("High value deal. Use safer payment terms.")

        score = max(0, min(score, 100))

        if score >= 80:
            risk_level = "Low"
            payment_recommendation = "Proceed with standard payment terms."
            advance_recommendation = "30% to 50% advance is acceptable."
        elif score >= 60:
            risk_level = "Medium"
            payment_recommendation = "Proceed with caution and written agreement."
            advance_recommendation = "50% to 70% advance recommended."
        else:
            risk_level = "High"
            payment_recommendation = "Avoid credit sale. Use advance or escrow only."
            advance_recommendation = "80% to 100% advance recommended."

        return TrustResult(
            counterparty_name=request.counterparty_name,
            trust_score=score,
            risk_level=risk_level,
            payment_recommendation=payment_recommendation,
            advance_recommendation=advance_recommendation,
            warnings=warnings,
            next_actions=[
                "Verify GST/PAN or FPO registration where applicable.",
                "Use written deal agreement before dispatch.",
                "Confirm payment mode before loading produce.",
                "Record delivery proof and quality acceptance.",
            ],
        )


if __name__ == "__main__":
    agent = TrustAgent()

    result = agent.evaluate(
        TrustRequest(
            counterparty_name="FreshAgro Retail Buyer",
            counterparty_type="Buyer",
            location="Kolkata",
            deal_value=23000,
            previous_deals_count=12,
            on_time_payment_rate=92,
            dispute_count=0,
            verified=True,
        )
    )

    print(result)
