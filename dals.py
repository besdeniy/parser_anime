from itertools import groupby

from repository import AnimeRepository


class AnimeDal:
    @staticmethod
    def return_anime_list(anime_data_all):    # for all_anime_data
        create_data = anime_data_all

        key = lambda x: x['id']

        create_data = sorted(create_data, key=key)          # sort first data

        result_list_anime = []

        for key_data, raw_data in groupby(create_data, key=key):
            anime_dict = dict()
            genres_set = set()
            urls_set = set()

            for data in raw_data:
                if data.url is not None:
                    urls_set.add(data.url)
                genres_set.add(data.genre)

            anime_dict = data._asdict()
            anime_dict['genre'] = list(genres_set)
            urls_set = list(urls_set)

            if urls_set == []:
                urls_set = None

            anime_dict['url'] = urls_set

            result_list_anime.append(anime_dict)

        return result_list_anime


if __name__ == "__main__":

    AnimeDal.return_anime_list(AnimeRepository.get_anime_all())
