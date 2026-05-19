from fastapi import APIRouter
from app.models.tourist import TouristCreate
from app.database import db
from app.blockchain import add_block
import uuid

router = APIRouter(prefix="/tourist", tags=["Tourist"])


@router.post("/register")
async def register_tourist(tourist: TouristCreate):

    tourist_id = str(uuid.uuid4())

    data = tourist.dict()
    data["tourist_id"] = tourist_id
    data["safety_score"] = 100

    await db.tourists.insert_one(data)

    blockchain_record = add_block(data)

    return {
        "message": "Tourist Registered Successfully",
        "tourist_id": tourist_id,
        "blockchain_hash": blockchain_record["hash"]
    }


@router.get("/{tourist_id}")
async def get_tourist(tourist_id: str):

    tourist = await db.tourists.find_one({
        "tourist_id": tourist_id
    })

    if tourist:
        tourist.pop("_id")

    return tourist
