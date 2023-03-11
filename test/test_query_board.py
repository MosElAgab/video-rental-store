from src.query_board import (get_movies)
import pytest


# test get_movies
def test_get_movies_return_a_list_of__dictionaries():
    movies = get_movies()
    assert isinstance(movies, list)
    assert isinstance(movies[0], dict)


def test_get_movies_return_a_list_of_dictionaries_of_all_movies():
    movies = get_movies()
    assert len(movies) == 25


def test_get_movies_returns_a_list_of_dictionaries_with_the_correct_keys():
    movies = get_movies()
    VALID_KEYS = ['movie_id', 'title', 'release_date', 'rating', 'cost', 'classification']
    returned_keys = [key for key, value in movies[0].items()]
    for i in range(0, len(VALID_KEYS)):
        assert VALID_KEYS[i] in returned_keys


def test_default_order_of_the_movies_should_be_alphabetically_by_title():
    movies = get_movies()
    assert movies[0]['title'] == 'A Fish Called Wanda'


def test_it_accepts_a_release_date_sort_by_parameter():
    movies = get_movies(sort_by='release_date')
    assert str(movies[0]['release_date']) == '1963-07-31'
    assert str(movies[24]['release_date']) == '2019-12-20'


def test_it_accepts_a_rating_sort_by_parameter():
    movies = get_movies(sort_by='rating')
    assert movies[0]['rating'] == 0
    assert movies[24]['rating'] == 10


def test_it_accepts_a_cost_sort_by_parameter():
    movies = get_movies(sort_by='cost')
    assert movies[0]['cost'] == 1
    assert movies[24]['cost'] == 2.5


def test_it_only_accepts_valid_sort_by_parameters():
    with pytest.raises(KeyError, match='Invalid sort-by key'):
        get_movies(sort_by='movie_id')


def test_it_accept_ASC_or_DESC_order_argument_and_returns_data_accordingly():
    movies = get_movies(order='ASC')
    assert movies[0]['title'] == 'A Fish Called Wanda'
    assert movies[24]['title'] == 'Tron'
    movies = get_movies(order='DESC')
    assert movies[0]['title'] == 'Tron'
    assert movies[24]['title'] == 'A Fish Called Wanda'
    movies = get_movies(sort_by='rating', order='ASC')
    assert movies[0]['rating'] == 0
    movies = get_movies(sort_by='rating', order='DESC')
    assert movies[0]['rating'] == 10
    movies = get_movies(sort_by='release_date', order='DESC')
    assert str(movies[0]['release_date']) == '2019-12-20'
    movies = get_movies(sort_by='cost', order='DESC')
    assert movies[0]['cost'] == 2.5


def test_it_throws_KeyError_when_invalid_order_key_passed_on():
    with pytest.raises(KeyError, match='Invalid order key'):
        get_movies(order='OO')


def test_it_accepts_min_rating_argument_which_filters_movies_to_those_has_higher_or_equal_rating():
    min_rating = 8
    movies = get_movies(min_rating=min_rating, sort_by='rating')
    for i, movie in enumerate(movies):
        if movie['rating'] < min_rating:
            assert False
        if i == (len(movies) - 1):
            assert True


def test_it_throws_TypeError_if_non_int_is_passed_as_min_rating_arg():
    with pytest.raises(TypeError, match='Invalid min rating data type'):
        get_movies(min_rating=[])
    with pytest.raises(TypeError, match='Invalid min rating data type'):
        get_movies(min_rating='')


def test_it_throws_error_if_min_rating_arg_is_out_of_range_value():
    with pytest.raises(ValueError, match='min rating out of range'):
        get_movies(min_rating=11)


def test_it_accepts_optional_location_argument_that_filters_movies_by_store():
    movies = get_movies(location='Manchester')
    print(type(movies[0]['cost']))
    assert len(movies) == 5
    movies = get_movies(location='Leeds')
    assert len(movies) == 5
    movies = get_movies(location='Birmingham')
    assert len(movies) == 4
    movies = get_movies(location='Newcastle')
    assert len(movies) == 3


def test_it_throws_error_if_invalid_location_data_type_passed_on():
    with pytest.raises(TypeError):
        get_movies(location=1879)
    with pytest.raises(Exception):
        get_movies(location='abcdefghijklmnopqrstuskoskdai')


# test apply discount
def test_it_throws_TypeError_if_none_int_was_passed():
    pass


def test_it_throws_ValueError_if_out_of_range_was_passed():
    pass


def test_it_returns_a_list_of_dictionaries_with_new_discounted_data():
    pass


def test_it_update_movies_table_from_the_database():
    pass
