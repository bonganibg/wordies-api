from pydantic import BaseModel

class Attempt(BaseModel):
    word: str
    letters: list[str]