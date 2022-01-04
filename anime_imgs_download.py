import requests
from lxml import html
import os
from time import sleep


class ImgsDownload:

    @classmethod
    def main(cls,list_queries):
        for query in list_queries:
            if '/' in  query:
                query = query.replace('/',':')
            print('start')
            cod_str = cls.get_html_cod(query)
            tree_html = cls.parse_data_from_avito(cod_str)
            cls.download_imgs(tree_html, query)
            print('end')

    @staticmethod
    def get_html_cod(query):
        """
        функция которая получает код страницы
        :param search: данные по которым ведется поиск
        :return: cod_str
        """
        url = 'https://yandex.ru/images/search?text='
        list_n = query.lower().split()
        query = '%20'.join(list_n)
        rez_url = f'{url}{query}'
        print(rez_url)
        cod_str_abrakadabra = requests.get(rez_url)
        return cod_str_abrakadabra

    @staticmethod
    def parse_data_from_avito(code_str):
        tree = html.fromstring(code_str.content)
        return tree

    @staticmethod
    def download_imgs(tree,query):
        a = [x.attrib['src'] for x in tree.cssselect('img') if 'images' in x.attrib['src']]
        #a = tree.xpath('//div[@class="serp-item__preview"]/a/@href')
        sleep(0.3)
        print(a)
        s = len(a)
        os.mkdir(f'images/{query.lower()}')
        for pic_link in a:
            sleep(1)
            with open(f'images/{query.lower()}/{s}.jpg', 'wb+') as f:
                pic_link = f"http:{pic_link}"
                f.write(requests.get(pic_link).content)
                s -= 1


if __name__ == '__main__':
    list_queries = ['рыбалка зимняя/русская', 'рыбалка на щуку', 'рыбалка спининг']
    ImgsDownload.main(list_queries)