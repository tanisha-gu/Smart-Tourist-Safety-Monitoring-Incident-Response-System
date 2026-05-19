class AIEngine:

    @staticmethod
    def detect_anomaly(last_seen_minutes, route_deviation_km):

        risk_score = 0

        if last_seen_minutes > 60:
            risk_score += 40

        if route_deviation_km > 10:
            risk_score += 30

        if last_seen_minutes > 180:
            risk_score += 50

        if risk_score >= 70:
            return {
                "status": "HIGH_RISK",
                "message": "Tourist may be in distress"
            }

        elif risk_score >= 40:
            return {
                "status": "MEDIUM_RISK",
                "message": "Suspicious movement detected"
            }

        return {
            "status": "SAFE",
            "message": "No anomaly detected"
        }
