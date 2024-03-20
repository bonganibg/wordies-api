from src.services.game_logic import GameLogicService
from src.models.round import Round
from src.models.attempt import Attempt

class GameController():
    file_words = "./resources/words.txt"

    def __init__(self) -> None:
        self.__game_logic = GameLogicService(self.file_words)

    def get_round_details(self, level: int) -> list:
        letters = self.__game_logic.generate_valid_random_letters(level)
        possible_words = self.__game_logic.get_total_possible_words(letters)
        return Round(letters=letters, possible_words_count=possible_words, level=level)
    
    def get_score(self, attempt: Attempt) -> int:
        return self.__game_logic.get_score(attempt.word, attempt.letters)
    

    

        