class BuyerOnboardingVerificationAgent:
    def status(self):
        return {
            "agent": "Buyer Onboarding / Buyer Verification Agent",
            "status": "planned",
            "classification": "RESTRICTED buyer commercial trust data",
            "rule": "Use public data plus explicit onboarding/verification. Do not scrape private buyer contact data behind login.",
        }
