from fastapi import APIRouter
from app.database import db

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


@router.get("/statistics")
async def dashboard_statistics():

    tourists = await db.tourists.count_documents({})
    alerts = await db.alerts.count_documents({})
    locations = await db.locations.count_documents({})

    return {
        "total_tourists": tourists,
        "total_alerts": alerts,
        "tracked_locations": locations
    }
