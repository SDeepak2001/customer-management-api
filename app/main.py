from fastapi import FastAPI
from .database import engine, Base
from .routes import router

# Create all tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# Include API routes
app.include_router(router)
