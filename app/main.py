from fastapi import FastAPI

from app.config import settings

app = FastAPI(title="lab-server")


@app.get("/health")
def health() -> dict[str, bool]:
    return {"ok": True}
