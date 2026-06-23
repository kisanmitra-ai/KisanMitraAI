class CommodityNormalizationAgent:
    """
    Module 17A.
    India-ready commodity and unit normalization.
    Deterministic backend logic only.
    """

    COMMODITY_ALIASES = {
        "potato": "POTATO",
        "aloo": "POTATO",
        "alu": "POTATO",
        "आलू": "POTATO",
        "আলু": "POTATO",

        "onion": "ONION",
        "pyaz": "ONION",
        "pyaaz": "ONION",
        "kanda": "ONION",
        "प्याज": "ONION",

        "tomato": "TOMATO",
        "tamatar": "TOMATO",
        "टमाटर": "TOMATO",

        "brinjal": "BRINJAL",
        "baingan": "BRINJAL",
        "begun": "BRINJAL",
        "बैंगन": "BRINJAL",
        "বেগুন": "BRINJAL",

        "wheat": "WHEAT",
        "gehun": "WHEAT",
        "गेहूं": "WHEAT",

        "paddy": "PADDY",
        "rice paddy": "PADDY",
        "dhan": "PADDY",
        "धान": "PADDY",

        "soybean": "SOYBEAN",
        "soya": "SOYBEAN",

        "cotton": "COTTON",
        "kapas": "COTTON",

        "mustard": "MUSTARD",
        "sarson": "MUSTARD",
        "सरसों": "MUSTARD",

        "chilli": "CHILLI",
        "mirchi": "CHILLI",
        "मिर्च": "CHILLI",

        "banana": "BANANA",
        "kela": "BANANA",
        "केला": "BANANA",
    }

    UNIT_ALIASES = {
        "quintal": "QUINTAL",
        "quintals": "QUINTAL",
        "qtl": "QUINTAL",
        "q": "QUINTAL",
        "क्विंटल": "QUINTAL",

        "kg": "KG",
        "kgs": "KG",
        "kilogram": "KG",
        "kilograms": "KG",

        "tonne": "TONNE",
        "ton": "TONNE",
        "metric ton": "TONNE",
        "mt": "TONNE",
    }

    def _canon(self, value):
        return str(value or "").strip()

    def normalize_commodity(self, value):
        raw = self._canon(value)
        key = raw.lower()
        canonical = self.COMMODITY_ALIASES.get(key)

        if not canonical and raw:
            canonical = raw.upper().replace(" ", "_").replace("-", "_")

        return {
            "raw": raw,
            "canonical": canonical,
            "known": key in self.COMMODITY_ALIASES,
        }

    def normalize_unit(self, value):
        raw = self._canon(value)
        key = raw.lower()
        canonical = self.UNIT_ALIASES.get(key)

        if not canonical and raw:
            canonical = raw.upper().replace(" ", "_").replace("-", "_")

        return {
            "raw": raw,
            "canonical": canonical,
            "known": key in self.UNIT_ALIASES,
        }
