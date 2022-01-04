import pytest
import sys
sys.path.append("../parser_anime")

from parser_anime_data import DataSearched


def test_parser_genres_all():       # test for function DataSearched.parser_genres_all

    with open('Saved_cod_page.txt', 'r', encoding="utf-8") as file:
        code_str = file.read()
    tree = DataSearched.convert_to_tree(code_str)

    list_genres = ['Экшен', 'Боевые искусства', 'Вампиры', 'Война', 'Гарем', 'Гарем для девушек', 'Гендерная интрига', 'Детектив', 'Дзёсэй', 'Драма', 'Игра', 'История', 'Киберпанк', 'Комедия', 'Лесби-тема', 'Меха', 'Мистика', 'Пародия', 'Повседневность', 'Постапокалиптика', 'Приключения', 'Психология', 'Романтика', 'Самурайский боевик', 'Сверхъестественное', 'Сёдзё', 'Сёнэн', 'Спорт', 'Сэйнэн', 'Трагедия', 'Триллер', 'Ужасы', 'Фантастика', 'Фэнтези', 'Школа', 'Этти']

    test_list_genres = DataSearched.parser_genres_all(tree)

    assert test_list_genres == list_genres