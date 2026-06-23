
class LogisticsCostAgent:
    """
    MVP logistics estimator.
    Later this will connect to route, vehicle and shared transport marketplace.
    """

    def estimate(self, distance_km=10, quantity_kg=1000, vehicle_type="mini_truck", buyer_pickup=False):
        if buyer_pickup:
            return {
                "vehicle_type": "buyer_pickup",
                "distance_km": distance_km,
                "transport_cost": 0,
                "loading_cost": round(quantity_kg * 0.25, 2),
                "unloading_cost": 0,
                "route_risk": "low",
                "note": "Buyer pickup reduces farmer transport cost.",
            }

        base_cost_by_vehicle = {
            "small_van": 1200,
            "mini_truck": 1800,
            "pickup": 1500,
            "truck": 4500,
        }

        per_km_by_vehicle = {
            "small_van": 22,
            "mini_truck": 32,
            "pickup": 28,
            "truck": 55,
        }

        base_cost = base_cost_by_vehicle.get(vehicle_type, 1800)
        per_km = per_km_by_vehicle.get(vehicle_type, 32)

        transport_cost = round(base_cost + (distance_km * per_km), 2)
        loading_cost = round(quantity_kg * 0.25, 2)
        unloading_cost = round(quantity_kg * 0.20, 2)

        route_risk = "low"
        if distance_km > 80:
            route_risk = "medium"
        if distance_km > 160:
            route_risk = "high"

        return {
            "vehicle_type": vehicle_type,
            "distance_km": distance_km,
            "transport_cost": transport_cost,
            "loading_cost": loading_cost,
            "unloading_cost": unloading_cost,
            "route_risk": route_risk,
            "note": "MVP logistics estimate. Replace with route API and transporter marketplace later.",
        }
