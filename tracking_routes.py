from fastapi import APIRouter
from app.models.tourist import TouristLocation
from app.database import db
from app.geofence import is_inside_restricted_zone
from app.ai_engine import AIEngine
from datetime import datetime

router = APIRouter(prefix="/tracking", tags=["Tracking"])


@router.post("/update-location")
async def update_location(location: TouristLocation):

    location_data = {
        "tourist_id": location.tourist_id,
        "latitude": location.latitude,
        "longitude": location.longitude,
        "timestamp": datetime.utcnow()
    }

    await db.locations.insert_one(location_data)

    restricted = is_inside_restricted_zone(
        location.latitude,
        location.longitude
    )

    ai_result = AIEngine.detect_anomaly(
        last_seen_minutes=70,
        route_deviation_km=12
    )

    return {
        "location_saved": True,
        "restricted_zone": restricted,
        "ai_analysis": ai_result
    }
