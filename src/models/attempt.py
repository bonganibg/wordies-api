from pydantic import BaseModel

class Attempt(BaseModel):
    words: str
    letters: list[str]