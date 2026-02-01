from fastapi import FastAPI
from sqlalchemy import text
from db.session import engine

app = FastAPI(title="UlechuBot", version="0.0.1")


@app.get("/ping")
async def pong():
    return {"ping": "pong", "message": "System is operationalwww"}


@app.get("/health")
async def health_check():
    try:
        async with engine.connect() as conn:
            await conn.execute(text("SELECT 1"))
        return {"databse": "online", "status": "healthy🟢"}
    except Exception as e:
        return {"databse": "offline", "error": str(e), "status": "critical 🔴"}
