from fastapi import FastAPI
from parser_anime_data import DataSearched
import pydantic_shema as pchema
from anime_imgs_download import ImgsDownload
from repository import AnimeRepository, GenreRepository
from dals import AnimeDal
app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get('/anime_all_data',response_model=pchema.AnimeAll)
def show_anime():
    list_all_anime = AnimeRepository.get_anime_all()

    group_list_anime = AnimeDal.return_anime_list(list_all_anime)

    json_small = [pchema.AnimeOne.parse_obj(x) for x in group_list_anime]

    all_data = pchema.AnimeAll(anime_list=json_small)

    return all_data


@app.get('/anime_all_genres',response_model=pchema.GenresAll)
def show_anime():
    all_genres = GenreRepository.get_all_ganres()
    end_list = []

    for i in all_genres:
        end_list.append(i[0])

    data = {}
    data['genres'] = end_list
    json_all_genres = pchema.GenresAll(**data)

    return json_all_genres


@app.get("/anime_genres/{genre_id}", response_model=pchema.AnimeAll)
def read_item(genre_id: int):
    list_anime_with_genre = AnimeRepository.get_anime_with_genre(genre_id)

    group_list_anime = AnimeDal.return_anime_list(list_anime_with_genre)

    json_small = [pchema.AnimeOne.parse_obj(x) for x in group_list_anime]

    all_data_with_genre = pchema.AnimeAll(anime_list=json_small)

    return all_data_with_genre


@app.get("/anime_id/{anime_id}", response_model=pchema.AnimeAll)
def read_item(anime_id: int):
    list_anime = AnimeRepository.get_anime_with_id(anime_id)

    anime = AnimeDal.return_anime_list(list_anime)

    json_small = [pchema.AnimeOne.parse_obj(x) for x in anime]

    all_data_anime_one = pchema.AnimeAll(anime_list=json_small)

    return all_data_anime_one


# @app.get("/title", response_model=pchema.AllAnimeName)
# def show_title():
#     anime_data = DataSearched.main('https://animestars.org/topanime.html')
#     list_h = []
#     for anime in anime_data:
#         a = {}
#         a['name'] = anime['name']
#         json_small = pchema.AnimeOneName(**a)
#         list_h.append(json_small)
#     result = pchema.AllAnimeName(all_anime=list_h)
#     return result
#
