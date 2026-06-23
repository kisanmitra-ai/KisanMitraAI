"""
KisanMitraAI Buyer Onboarding Agent

Purpose:
- Register buyers
- Capture business profile
- Capture crop demand profile
- Check basic onboarding completeness
- Prepare buyer for verification and deal access
"""

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class BuyerOnboardingRequest:
    business_name: str
    buyer_name: str
    mobile: str
    location: str
    buyer_type: str
    preferred_crops: List[str]
    preferred_quality: Optional[str] = "B"
    delivery_preference: Optional[str] = "Pickup or delivery"
    payment_preference: Optional[str] = "UPI/Bank transfer"


@dataclass
class BuyerOnboardingResult:
    buyer_id: str
    business_name: str
    onboarding_status: str
    verification_status: str
    demand_profile_status: str
    missing_fields: List[str]
    next_actions: List[str]


class BuyerOnboardingAgent:

    def onboard(self, request: BuyerOnboardingRequest) -> BuyerOnboardingResult:
        missing = []

        if not request.business_name:
            missing.append("business_name")
        if not request.buyer_name:
            missing.append("buyer_name")
        if not request.mobile:
            missing.append("mobile")
        if not request.location:
            missing.append("location")
        if not request.buyer_type:
            missing.append("buyer_type")
        if not request.preferred_crops:
            missing.append("preferred_crops")

        buyer_id = "KM-BUYER-DRAFT-001"

        onboarding_status = "Incomplete" if missing else "Draft buyer profile ready"
        verification_status = "Pending KYC/GST/PAN verification"
        demand_profile_status = "Ready" if request.preferred_crops else "Missing crop demand"

        return BuyerOnboardingResult(
            buyer_id=buyer_id,
            business_name=request.business_name,
            onboarding_status=onboarding_status,
            verification_status=verification_status,
            demand_profile_status=demand_profile_status,
            missing_fields=missing,
            next_actions=[
                "Collect GST/PAN or business registration if applicable.",
                "Run Buyer Onboarding Verification Agent.",
                "Create buyer demand profile for crop, quality, quantity and region.",
                "Run Trust Engine before allowing high-value negotiation.",
                "Keep direct farmer contact blocked until admin approval.",
            ],
        )


if __name__ == "__main__":
    agent = BuyerOnboardingAgent()

    result = agent.onboard(
        BuyerOnboardingRequest(
            business_name="FreshAgro Retail Buyer",
            buyer_name="Procurement Manager",
            mobile="Hidden for privacy",
            location="Kolkata, West Bengal",
            buyer_type="Retail Aggregator",
            preferred_crops=["Tomato", "Potato", "Onion"],
            preferred_quality="A",
        )
    )

    print(result)
