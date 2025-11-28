from fastapi import FastAPI
from src.routes import router as api_router

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    # Initialize database connection here if needed
    pass

@app.on_event("shutdown")
async def shutdown_event():
    # Close database connection here if needed
    pass

app.include_router(api_router)