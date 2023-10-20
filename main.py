import uvicorn
from fastapi import FastAPI

from config import settings
from routers import PDBAPI, InterfaceAPI


app = FastAPI()
app.include_router(PDBAPI.pdbRouter)
app.include_router(InterfaceAPI.interfaceRouter)

@app.get("/info")
async def info():
    return {
        "app_name": settings.app_name,
        "debug": settings.debug,
        "file_root": settings.file_root,
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
