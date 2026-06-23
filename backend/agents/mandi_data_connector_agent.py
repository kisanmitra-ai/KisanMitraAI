class MandiDataConnectorAgent:
    """
    Module 17A.
    Source registry for MVP and future connectors.
    """

    def list_sources(self):
        return [
            {
                "source_key": "manual_official_csv",
                "source_name": "Manual Official CSV Upload",
                "scope": "India-wide",
                "classification": "PUBLIC",
                "access_mode": "manual_csv",
                "status": "active",
            },
            {
                "source_key": "agmarknet_future",
                "source_name": "Agmarknet official/public connector",
                "scope": "India-wide",
                "classification": "PUBLIC",
                "access_mode": "future_connector",
                "status": "planned",
            },
            {
                "source_key": "enam_future",
                "source_name": "eNAM official/public connector",
                "scope": "India-wide",
                "classification": "PUBLIC",
                "access_mode": "future_connector",
                "status": "planned",
            },
        ]
