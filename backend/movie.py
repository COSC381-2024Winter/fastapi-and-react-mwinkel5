# Model in MVC
from typing import Union, List
from pydantic import BaseModel

class Movie(BaseModel):
    id: int
    name: str
    cast: list