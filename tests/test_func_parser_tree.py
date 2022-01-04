import pytest
import sys
sys.path.append("../parser_anime")

from parser_anime_data import DataSearched


def test_parser_genres_all():       # test for function DataSearched.parser_tree

    with open('Saved_cod_page.txt', 'r', encoding="utf-8") as file:
        code_str = file.read()
    tree = DataSearched.convert_to_tree(code_str)

    with open('Saved_list_data_anime.txt', 'r', encoding="utf-8") as fil:
        list_data_anime = fil.read()

    test_list_data_anime = DataSearched.parser_tree(tree)

    assert str(test_list_data_anime) == list_data_anime