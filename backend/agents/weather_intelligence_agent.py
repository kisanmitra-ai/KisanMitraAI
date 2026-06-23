"""
KisanMitraAI Weather Intelligence Agent

Purpose:
- Convert weather data into crop-specific action intelligence
- Support disease risk, pest risk, irrigation, spray window, harvest window and daily tasks

MVP:
Uses supplied weather values.
Later:
Connect IMD, OpenWeather, WeatherAPI, NASA POWER or other verified providers.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class WeatherIntelligenceRequest:
    location: str
    crop: Optional[str] = None
    crop_stage: Optional[str] = None
    temperature_c: Optional[float] = None
    humidity_percent: Optional[float] = None
    rain_chance_percent: Optional[float] = None
    wind_kmph: Optional[float] = None
    forecast_hours: Optional[int] = 24


@dataclass
class WeatherIntelligenceResult:
    location: str
    crop: Optional[str]
    weather_summary: Dict
    disease_risk: str
    pest_risk: str
    irrigation_advice: str
    spray_window: str
    harvest_risk: str
    alerts: List[str]
    next_actions: List[str]
    safety_notes: List[str]


class WeatherIntelligenceAgent:

    def analyze(self, request: WeatherIntelligenceRequest) -> WeatherIntelligenceResult:
        temp = request.temperature_c
        humidity = request.humidity_percent
        rain = request.rain_chance_percent
        wind = request.wind_kmph

        alerts = []

        disease_risk = "Unknown"
        pest_risk = "Unknown"
        irrigation_advice = "Weather data incomplete. Cannot give irrigation advice."
        spray_window = "Weather data incomplete. Cannot confirm spray window."
        harvest_risk = "Unknown"

        if humidity is not None and rain is not None:
            if humidity >= 75 and rain >= 50:
                disease_risk = "High"
                alerts.append("High humidity and rain chance may increase fungal or bacterial disease risk.")
            elif humidity >= 65 or rain >= 35:
                disease_risk = "Medium"
            else:
                disease_risk = "Low"

        if temp is not None:
            if temp >= 34:
                pest_risk = "Medium to High"
                alerts.append("High temperature may increase pest activity and plant stress.")
            elif temp >= 28:
                pest_risk = "Medium"
            else:
                pest_risk = "Low"

        if temp is not None and rain is not None:
            if rain >= 60:
                irrigation_advice = "Avoid irrigation now unless soil is very dry. Rain is likely."
            elif temp >= 34 and rain < 30:
                irrigation_advice = "Check soil moisture. Irrigate during cooler hours if crop needs water."
            else:
                irrigation_advice = "Maintain normal irrigation based on soil moisture."

        if rain is not None and wind is not None:
            if rain >= 40:
                spray_window = "Poor spray window. Rain may wash off spray."
            elif wind >= 18:
                spray_window = "Poor spray window. Wind may cause drift."
            else:
                spray_window = "Possible spray window, but follow label, PPE and waiting-period safety rules."

        if rain is not None:
            if rain >= 60:
                harvest_risk = "High"
                alerts.append("Avoid harvest or drying-sensitive operations if heavy rain is likely.")
            elif rain >= 35:
                harvest_risk = "Medium"
            else:
                harvest_risk = "Low"

        weather_summary = {
            "temperature_c": temp,
            "humidity_percent": humidity,
            "rain_chance_percent": rain,
            "wind_kmph": wind,
            "forecast_hours": request.forecast_hours,
            "crop_stage": request.crop_stage,
        }

        next_actions = [
            "Connect live weather provider.",
            "Use GPS location for automatic village-level forecast.",
            "Send rain, spray and disease-risk alerts to farmer home screen.",
            "Connect to Daily Task Engine.",
            "Store weather events in Crop Passport.",
        ]

        safety_notes = [
            "Weather-based advice is advisory and depends on forecast accuracy.",
            "Do not spray chemicals before rain or in strong wind.",
            "Chemical advice must pass safety review before farmer-facing recommendation.",
            "Irrigation advice should be checked with actual soil moisture.",
        ]

        return WeatherIntelligenceResult(
            location=request.location,
            crop=request.crop,
            weather_summary=weather_summary,
            disease_risk=disease_risk,
            pest_risk=pest_risk,
            irrigation_advice=irrigation_advice,
            spray_window=spray_window,
            harvest_risk=harvest_risk,
            alerts=alerts,
            next_actions=next_actions,
            safety_notes=safety_notes,
        )


if __name__ == "__main__":
    agent = WeatherIntelligenceAgent()

    result = agent.analyze(
        WeatherIntelligenceRequest(
            location="Nadia, West Bengal",
            crop="Tomato",
            crop_stage="Flowering",
            temperature_c=34,
            humidity_percent=78,
            rain_chance_percent=55,
            wind_kmph=12,
        )
    )

    print(result)
