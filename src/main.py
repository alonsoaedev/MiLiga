# built-in

# third-party
from fastapi import FastAPI

# own

app = FastAPI()

@app.get("/api/v1/health")
async def health():
    return {"status": "ok"}
