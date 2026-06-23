class GeographyNormalizationAgent:
    """
    Module 17A.
    India-ready state/district/mandi normalization.
    Does not restrict data to one state or one crop.
    """

    STATE_ALIASES = {
        "wb": "WEST_BENGAL",
        "west bengal": "WEST_BENGAL",
        "পশ্চিমবঙ্গ": "WEST_BENGAL",

        "maharashtra": "MAHARASHTRA",
        "mh": "MAHARASHTRA",

        "karnataka": "KARNATAKA",
        "ka": "KARNATAKA",

        "uttar pradesh": "UTTAR_PRADESH",
        "up": "UTTAR_PRADESH",

        "punjab": "PUNJAB",
        "pb": "PUNJAB",

        "madhya pradesh": "MADHYA_PRADESH",
        "mp": "MADHYA_PRADESH",

        "gujarat": "GUJARAT",
        "gj": "GUJARAT",

        "rajasthan": "RAJASTHAN",
        "rj": "RAJASTHAN",

        "andhra pradesh": "ANDHRA_PRADESH",
        "ap": "ANDHRA_PRADESH",

        "tamil nadu": "TAMIL_NADU",
        "tn": "TAMIL_NADU",

        "bihar": "BIHAR",
        "odisha": "ODISHA",
        "telangana": "TELANGANA",
        "kerala": "KERALA",
        "assam": "ASSAM",
        "haryana": "HARYANA",
        "jharkhand": "JHARKHAND",
        "chhattisgarh": "CHHATTISGARH",
        "uttarakhand": "UTTARAKHAND",
        "himachal pradesh": "HIMACHAL_PRADESH",
    }

    def normalize_state(self, value):
        raw = str(value or "").strip()
        key = raw.lower()
        canonical = self.STATE_ALIASES.get(key) or raw.upper().replace(" ", "_").replace("-", "_")
        return {
            "raw": raw,
            "canonical": canonical,
            "known": bool(raw),
        }

    def normalize_district(self, value):
        raw = str(value or "").strip()
        canonical = raw.upper().replace(" ", "_").replace("-", "_") if raw else ""
        return {
            "raw": raw,
            "canonical": canonical,
            "known": bool(raw),
        }

    def normalize_mandi(self, value):
        raw = str(value or "").strip()
        canonical = " ".join(raw.split()).title() if raw else ""
        return {
            "raw": raw,
            "canonical": canonical,
            "known": bool(raw),
        }
