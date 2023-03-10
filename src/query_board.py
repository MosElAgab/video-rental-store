import pg8000.native as pg
import getpass
# from datetime import datetime as dt

username = getpass.getuser()
database = 'business_data'
conn = pg.Connection(username, database=database)


def get_movies(order='ASC', sort_by='title'):
    valid_sort_by_options = ['release_date', 'rating', 'cost', 'title']
    valid_order_keys = ['ASC', 'DESC']
    if sort_by not in valid_sort_by_options:
        raise KeyError('Invalid sort-by key')
    if order not in valid_order_keys:
        raise KeyError('Invalid order key')
    movies = conn.run(f'SELECT movie_id, title, release_date, COALESCE(rating, 0) AS rating, cost, classification FROM movies ORDER BY {pg.identifier(sort_by)} {pg.identifier(order)}')
    titles = [title['name'] for title in conn.columns]
    movies_dictionaries = []
    for i, movie in enumerate(movies):
        movies_dictionaries.append({title: movies[i][k] for k, title in enumerate(titles)})
    return movies_dictionaries
