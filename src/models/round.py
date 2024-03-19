from pydantic import BaseModel

class Round(BaseModel):
    letters: list[str]
    possilbe_words_count: int
    level: int
