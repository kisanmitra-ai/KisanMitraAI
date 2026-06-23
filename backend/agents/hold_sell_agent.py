
class HoldSellAgent:
    """
    MVP hold-vs-sell logic.
    """

    def advise(self, crop, storage_available, perishability, weather_risk, price_trend="stable"):
        crop_lower = (crop or "").lower()

        if crop_lower in ["tomato", "brinjal", "green chilli", "leafy vegetable"]:
            return {
                "decision": "sell_now",
                "label": "Sell now",
                "reason": "Crop is perishable. Holding can increase spoilage and rejection risk.",
            }

        if crop_lower in ["potato", "onion"] and storage_available:
            if price_trend == "rising" and weather_risk != "high":
                return {
                    "decision": "sell_partial_hold_partial",
                    "label": "Sell 50%, hold 50%",
                    "reason": "Storage is available and price trend may improve. Avoid holding entire quantity.",
                }

            return {
                "decision": "sell_majority_now",
                "label": "Sell majority now",
                "reason": "Storage exists, but current buyer offer is safe. Sell majority and hold small quantity if needed.",
            }

        return {
            "decision": "sell_now",
            "label": "Sell now",
            "reason": "Storage or price-trend advantage is not strong enough to justify holding.",
        }
