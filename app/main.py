from  fastapi  import FastAPI

app = FastAPI(
title="UlechuBot",
version="0.0.1"
)

@app.get("/ping")
async   def pong():
    return {"ping": "pong", "message": "System is operationalwww"}
