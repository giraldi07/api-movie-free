from pydantic import BaseModel

class Movie(BaseModel):
    poster_src: str
    rating: float
    quality: str
    poster_href: str
    title: str
    release_date: str

class TVSeries(BaseModel):
    poster_src: str
    rating: float
    quality: str
    poster_href: str
    title: str
    release_date: str
    seasons: int

class Genre(BaseModel):
    entry_href: str
    name: str

class Release(BaseModel):
    entry_href: str
    name: str
