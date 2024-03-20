from pydantic import BaseModel

class Round(BaseModel):
    letters: list[str]
    possible_words_count: int
    level: int
