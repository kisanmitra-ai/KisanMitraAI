
class BuyerOfferAgent:
    """
    MVP confirmed buyer offer engine.
    Later this will use real buyer demand and pre-harvest booking data.
    """

    def get_best_offer(self, crop="Potato", quantity_kg=4000):
        return {
            "buyer_name": "Kalna Fresh Buyers",
            "buyer_type": "verified_direct_buyer",
            "location": "Kalna, Purba Bardhaman",
            "crop_required": crop,
            "quantity_required_kg": quantity_kg,
            "grade_required": "A/B",
            "price_per_kg": 12.0,
            "pickup_available": True,
            "payment_terms": "Payment within 24 hours after delivery confirmation",
            "offer_validity": "Today",
            "rejection_terms": "Visible damage above 15% may reduce price",
            "verified": True,
            "payment_history_score": 82,
            "pickup_reliability_score": 84,
            "rejection_rate_percent": 7,
        }
