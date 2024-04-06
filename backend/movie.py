# Model in MVC
from typing import Union, List
from pydantic import BaseModel

class Movie(BaseModel):
    name: str
    cast: list