from fastapi import APIRouter, Depends, HTTPException
from src.models.attempt import Attempt
from src.models.round import Round
from src.controllers.game import GameController

router = APIRouter(
    prefix="/api/v1/game",
    tags=["Game"]
)

game_controller = GameController()

@router.get("/words/{level}")
def get_words(level: int):
    return game_controller.get_round_details(level)

@router.get("/score")
def get_score(attempt: Attempt):
    result = game_controller.get_score(attempt)
    
    return {
        "is_valid": result > 0,
        "score": result
    }
