from fastapi import FastAPI
from .routers import projects  # Import the project routes
from .database import engine, Base
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
FRONT_URL = os.getenv("FRONT_URL")

# Initialize the FastAPI app
app = FastAPI()

# CORS configuration to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONT_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include project routes
app.include_router(projects.router)

@app.get("/")
async def read_root():
    return {"message": "Portfolio intializing !!"}
