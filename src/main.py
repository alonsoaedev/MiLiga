# built-in

# third-party
from fastapi import FastAPI

# own
from src.infrastructure.web.tournament_controller import router as tournament_router
from src.infrastructure.web.team_controller import router as team_router

app = FastAPI(
    title="Mi Liga API",
    description="API for managing sports tournaments",
    version="0.1.0"
)

app.include_router(tournament_router, prefix="/api/v1")
app.include_router(team_router, prefix="/api/v1")

@app.get("/api/v1/health")
async def health():
    return {"status": "ok"}
