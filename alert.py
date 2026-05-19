from pydantic import BaseModel


class AlertModel(BaseModel):
    tourist_id: str
    alert_type: str
    latitude: float
    longitude: float
