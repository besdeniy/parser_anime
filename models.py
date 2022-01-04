from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from bd import Base


class Anime(Base):    # table with anime data
    __tablename__ = 'anime'

    id = Column(Integer, primary_key=True, index=True)
    short_name = Column(String)
    name = Column(String)
    year = Column(String)
    text = Column(String)


class Genre(Base):     # table with genres
    __tablename__ = "genre"

    id = Column(Integer, primary_key=True, index=True)
    genre = Column(String)


class GenreToAnime(Base):   #many_to_many,  animes ---- genres
    __tablename__ = "genre_to_anime"

    id = Column(Integer, primary_key=True, index=True)
    anime_id = Column(Integer, ForeignKey('anime.id'))
    genre_id = Column(Integer, ForeignKey('genre.id'))


class ImgToAnime(Base):
    __tablename__ = 'img_to_anime'

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String)
    anime_id = Column(Integer, ForeignKey('anime.id'))