from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import (
    auth_routes,
    tourist_routes,
    tracking_routes,
    alert_routes,
    dashboard_routes
)

app = FastAPI(
    title="Smart Tourist Safety Monitoring System",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_routes.router)
app.include_router(tourist_routes.router)
app.include_router(tracking_routes.router)
app.include_router(alert_routes.router)
app.include_router(dashboard_routes.router)


@app.get("/")
async def root():
    return {
        "message": "Smart Tourist Safety Monitoring API Running"
    }
