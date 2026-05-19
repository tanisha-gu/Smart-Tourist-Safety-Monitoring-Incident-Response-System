from fastapi import APIRouter
from app.models.alert import AlertModel
from app.database import db
from datetime import datetime

router = APIRouter(prefix="/alerts", tags=["Alerts"])


@router.post("/panic")
async def panic_alert(alert: AlertModel):

    alert_data = {
        "tourist_id": alert.tourist_id,
        "alert_type": alert.alert_type,
        "latitude": alert.latitude,
        "longitude": alert.longitude,
        "time": datetime.utcnow(),
        "status": "ACTIVE"
    }

    await db.alerts.insert_one(alert_data)

    return {
        "message": "Emergency Alert Sent Successfully",
        "nearest_police_station": "Central Police Unit"
    }
