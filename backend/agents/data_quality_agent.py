from datetime import datetime, timezone, date


class DataQualityAgent:
    """
    Module 17A.
    Deterministic quality checks. No LLM arithmetic or validation.
    """

    CRITICAL_FLAGS = {
        "missing_modal_price",
        "missing_mandi_name",
        "missing_commodity",
        "invalid_date",
        "negative_price",
        "min_price_greater_than_max_price",
        "unknown_unit",
    }

    def parse_float(self, value):
        if value is None:
            return None

        text = str(value).strip()

        if not text:
            return None

        try:
            return float(text.replace(",", ""))
        except Exception:
            return None

    def parse_date(self, value):
        if not value:
            return None, "invalid_date"

        text = str(value).strip()

        for fmt in ("%Y-%m-%d", "%d-%m-%Y", "%d/%m/%Y"):
            try:
                parsed = datetime.strptime(text, fmt).date()
                return parsed, None
            except Exception:
                pass

        try:
            return date.fromisoformat(text), None
        except Exception:
            return None, "invalid_date"

    def validate(self, raw_row, normalized):
        flags = []

        if not normalized.get("mandi"):
            flags.append("missing_mandi_name")

        if not normalized.get("commodity"):
            flags.append("missing_commodity")

        if normalized.get("unit_known") is False:
            flags.append("unknown_unit")

        if normalized.get("commodity_known") is False:
            flags.append("unknown_commodity_alias")

        min_price = self.parse_float(raw_row.get("min_price"))
        modal_price = self.parse_float(raw_row.get("modal_price"))
        max_price = self.parse_float(raw_row.get("max_price"))
        arrival_quantity = self.parse_float(raw_row.get("arrival_quantity"))

        if modal_price is None:
            flags.append("missing_modal_price")

        for price in (min_price, modal_price, max_price):
            if price is not None and price < 0:
                flags.append("negative_price")

        if min_price is not None and max_price is not None and min_price > max_price:
            flags.append("min_price_greater_than_max_price")

        if arrival_quantity is None:
            flags.append("arrival_missing")

        parsed_date, date_error = self.parse_date(raw_row.get("price_date"))

        if date_error:
            flags.append(date_error)

        if parsed_date:
            age_days = (datetime.now(timezone.utc).date() - parsed_date).days
            if age_days > 30:
                flags.append("stale_data")

        critical_count = len([flag for flag in flags if flag in self.CRITICAL_FLAGS])
        warning_count = max(0, len(flags) - critical_count)

        confidence = 0.95 - (critical_count * 0.15) - (warning_count * 0.05)
        confidence = max(0.1, round(confidence, 2))

        is_suppressed = any(flag in self.CRITICAL_FLAGS for flag in flags) or "stale_data" in flags

        return {
            "flags": flags,
            "confidence_score": confidence,
            "is_suppressed": is_suppressed,
            "parsed": {
                "min_price": min_price,
                "modal_price": modal_price,
                "max_price": max_price,
                "arrival_quantity": arrival_quantity,
                "price_date": parsed_date.isoformat() if parsed_date else None,
            },
        }
