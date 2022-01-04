from sqlalchemy.orm import Session
from models import Anime, Genre, GenreToAnime, ImgToAnime


class AnimeRepository:
    @staticmethod
    def create_anime(short_name: str, name: str, year: str, text: str):
        session = Session()
        anime_object = Anime(short_name=short_name, name=name,
                             year=year, text=text)
        session.add(anime_object)
        session.commit()
        return anime_object

    @staticmethod
    def get_anime_id(name_anime: str):
        session = Session()
        anime_id = session.query(Anime.id).filter(Anime.short_name == name_anime).first()[0]
        session.commit()
        return anime_id

    @staticmethod
    def get_anime_all():   # funck for \anime_all_data
        session = Session()

        query = session.query(Anime.id, Anime.short_name, Anime.name, Genre.genre, Anime.year, Anime.text, ImgToAnime.url)

        query = query.join(GenreToAnime, GenreToAnime.anime_id == Anime.id)
        query = query.join(Genre, Genre.id == GenreToAnime.genre_id)
        query = query.outerjoin(ImgToAnime, ImgToAnime.anime_id == Anime.id)
        # import ipdb;  ipdb.set_trace()
        records = query
        return records

    @staticmethod
    def get_anime_with_genre(genre_id: int):
        session = Session()

        query = session.query(Anime.id, Anime.short_name, Anime.name, Genre.genre, Anime.year, Anime.text,
                              ImgToAnime.url).where(Genre.id == genre_id)
        query = query.join(GenreToAnime, GenreToAnime.anime_id == Anime.id)
        query = query.join(Genre, Genre.id == GenreToAnime.genre_id)
        query = query.outerjoin(ImgToAnime, ImgToAnime.anime_id == Anime.id)

        records = query
        return records

    @staticmethod
    def get_anime_with_id(anime_id: int):
        session = Session()

        query = session.query(Anime.id, Anime.short_name, Anime.name, Genre.genre, Anime.year, Anime.text,
                              ImgToAnime.url).where(Anime.id == anime_id)
        query = query.join(GenreToAnime, GenreToAnime.anime_id == Anime.id)
        query = query.join(Genre, Genre.id == GenreToAnime.genre_id)
        query = query.outerjoin(ImgToAnime, ImgToAnime.anime_id == Anime.id)
        # import ipdb;
        # ipdb.set_trace()
        # print()
        records = query
        return records


class GenreRepository:
    @staticmethod
    def create_genre(genre: str):
        session = Session()
        genre_object = Genre(genre=genre)
        session.add(genre_object)
        session.commit()
        return genre_object

    @staticmethod
    def get_ganre_id(name_genre: str):
        session = Session()
        genre_id = session.query(Genre.id).filter(Genre.genre == name_genre).first()
        session.commit()
        return genre_id

    @staticmethod
    def get_all_ganres():    # funck for \anime_all_genres
        session = Session()
        genres = session.query(Genre.genre)
        session.commit()
        return genres


class GenreToAnimeRepository:
    @staticmethod
    def create_table(id_anime, id_genre):
        session = Session()
        table = GenreToAnime(anime_id=id_anime, genre_id=id_genre)
        session.add(table)
        session.commit()
        return table


class ImgToAnimeRepository:
    @staticmethod
    def create_genre(url: str, anime_id):
        session = Session()
        img_object = ImgToAnime(url=url, anime_id=anime_id)
        session.add(img_object)
        session.commit()
        return img_object

