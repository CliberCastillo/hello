
from fastapi import FastAPI
import os

app = FastAPI(title="MiBanco API", version="1.0.0")

TEXT = os.getenv("TEXT", "hola mibanco :D")

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.get("/v1/mibanco")
async def mibanco():
    return {"message": TEXT}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)