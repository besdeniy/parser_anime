import requests
from lxml import html
from copy import deepcopy

from repository import AnimeRepository, GenreRepository, GenreToAnimeRepository, ImgToAnimeRepository


class DataSearched:
    @classmethod
    def main(cls, url):
        page_cod = cls.get_str_code(url)
        tree = cls.convert_to_tree(page_cod)
        list_data_all = cls.parser_tree(tree)
        list_genres_all = cls.parser_genres_all(tree)
        with open('Saved_cod_page.txt', 'w+', encoding="utf-8") as file:
            file.write(str(page_cod))
        with open('Saved_list_data_anime.txt', 'w+', encoding="utf-8") as file:
            file.write(str(str(list_data_all)))


        # for genre_one in list_genres_all:
        #     GenreRepository.create_genre(genre_one)
        #
        # for anime_one_dict in list_data_all:
        #
        #     anime = anime_one_dict["anime"]
        #     AnimeRepository.create_anime(**anime)
        #
        #     anime_name = anime['short_name']
        #     id_anime = AnimeRepository.get_anime_id(anime_name)
        #
        #     genres = anime_one_dict['genres']
        #     for g in genres:
        #
        #         id_genre = GenreRepository.get_ganre_id(g)
        #         if id_genre is None:
        #             continue
        #         id_genre = id_genre[0]
        #         i = GenreToAnimeRepository.create_table(id_anime, id_genre)
        #         print(i)
        #
        #     anime_img_urls = anime_one_dict['imgs']
        #
        #     if anime_img_urls == []:
        #         continue
        #     for url in anime_img_urls:
        #         i = ImgToAnimeRepository.create_genre(url, id_anime)
        #         print(i)

    @staticmethod
    def get_str_code(url):
        str_cod_abra = requests.get(url)
        page_cod = str_cod_abra.text
        return page_cod

    @staticmethod
    def convert_to_tree(page_cod):
        tree = html.fromstring(page_cod)
        return tree

    @classmethod
    def parser_tree(cls,tree):
        list_urls = tree.xpath('//div[@class="rels-shot short clearfix"]//@href')
        list_data_all = []
        for url_page_info in list_urls:
            tree_page_info = cls.convert_to_tree(cls.get_str_code(url_page_info))
            dict_data = cls.__extract_data(tree_page_info)
            list_data_all.append(dict_data)
        return list_data_all

    @classmethod
    def parser_genres_all(cls, tree):
        list_genres_all = tree.xpath("//ul[@class='flex-row']/li/a/text()")
        return list_genres_all

    @staticmethod
    def __extract_data(tree):
        tree = deepcopy(tree)
        dict_param = {}
        short_name = tree.xpath('//div[@class="btoom-title"]//text()')[0]
        name = tree.xpath('//div[@class="short-t-or"]//text()')[0]
        #series = tree.xpath("//div[@class = 'fi-col'][2]//div[@class='fi-col-item']/div[@class= 'sfull-t']/../span/text()")[0]
        genres = tree.xpath("//div[@class = 'fi-col'][2]//div[@class='fi-col-item']/a/text()")
        year = tree.xpath("//div[@class = 'fi-col'][1]/div[@class='fi-col-item']/a/text()")[0]
        text = tree.xpath("//div[@class='full-text clearfix video-box']/div[@itemprop = 'description']/p/text()")[0]
        imgs = tree.xpath('//ul[@class="xfieldimagegallery screens"]/li/a/@href')

        dict_param['short_name'] = short_name
        dict_param['name'] = name
        dict_param['year'] = year
        #dict_param['series'] = series
        dict_param['genres'] = genres
        dict_param['text'] = text
        result_data_anime = {
            'anime':{
                'short_name': short_name,
                'name': name,
                'year': year,
                'text': text
            },
            'genres': genres,
            'imgs': imgs
        }
        return result_data_anime


if __name__ == "__main__":
    url = "https://animestars.org/topanime.html"
    list_data = DataSearched.main(url)
    #print(list_data)