from pydantic import BaseModel, EmailStr


class TouristCreate(BaseModel):
    name: str
    passport_number: str
    nationality: str
    email: EmailStr
    emergency_contact: str
    itinerary: str


class TouristLocation(BaseModel):
    tourist_id: str
    latitude: float
    longitude: float
