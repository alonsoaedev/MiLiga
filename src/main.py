# built-in

# third-party
from fastapi import FastAPI

# own
from app.controllers.tournament import router as tournament_router

app = FastAPI()

@app.get("/api/v1/health")
async def health():
    return {"status": "ok"}

app.include_router(tournament_router)
