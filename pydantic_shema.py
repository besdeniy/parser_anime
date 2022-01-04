from pydantic import BaseModel
from typing import List, Optional


class AnimeOne(BaseModel):
    id: int
    short_name: str
    name: str
    genre: List[str]
    year: str
    text: str
    url: List[str] = None


class GenresAll(BaseModel):
    genres: List[str]


class AnimeAll(BaseModel):
    anime_list: List[AnimeOne]

