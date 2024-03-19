from fastapi import APIRouter
from src.routers import game

# Add routes
router = APIRouter()
router.include_router(game.router)

