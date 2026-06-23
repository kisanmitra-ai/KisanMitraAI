class ComplianceConsentAgent:
    """
    Module 17A.
    Public/restricted/private classification guard.
    """

    PRIVATE_FIELD_HINTS = {
        "phone",
        "mobile",
        "farmer_phone",
        "farmer_mobile",
        "aadhaar",
        "aadhar",
        "bank",
        "account",
        "ifsc",
        "pan",
        "upi",
        "private_contact",
    }

    RESTRICTED_FIELD_HINTS = {
        "buyer_rating",
        "buyer_score",
        "transaction_rating",
        "credit_score",
        "private_buyer_notes",
    }

    def classify_row(self, row):
        keys = {str(key).strip().lower() for key in row.keys()}

        private_hits = sorted(keys.intersection(self.PRIVATE_FIELD_HINTS))
        restricted_hits = sorted(keys.intersection(self.RESTRICTED_FIELD_HINTS))

        if private_hits:
            return {
                "classification": "PRIVATE",
                "allowed": False,
                "reason": "Private fields found: " + ", ".join(private_hits),
            }

        if restricted_hits:
            return {
                "classification": "RESTRICTED",
                "allowed": True,
                "reason": "Restricted commercial fields found; store only with audit and do not expose publicly.",
            }

        return {
            "classification": "PUBLIC",
            "allowed": True,
            "reason": "Mandi price and arrival data is public market data with source lineage.",
        }
