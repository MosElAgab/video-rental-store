import pg8000.native as pg
import getpass
# from datetime import datetime as dt

username = getpass.getuser()
database = 'business_data'


def get_movies(order='ASC', sort_by='title', min_rating=-1, location=None):
    conn = pg.Connection(username, database=database)
    if type(min_rating) is not int:
        raise TypeError('Invalid min rating data type')
    elif min_rating > 10 or min_rating < -1:
        raise ValueError('min rating out of range')
    valid_sort_by_options = ['release_date', 'rating', 'cost', 'title']
    valid_order_keys = ['ASC', 'DESC']
    if sort_by not in valid_sort_by_options:
        raise KeyError('Invalid sort-by key')
    if order not in valid_order_keys:
        raise KeyError('Invalid order key')
    if type(location) is not str and location is not None:
        raise TypeError
    elif location is not None and len(location) > 20:
        raise Exception
    movies = conn.run(f'SELECT movie_id, title, release_date, COALESCE(rating, 0) AS rating, cost, classification FROM movies WHERE COALESCE(rating, 0) >= :min_rating ORDER BY {pg.identifier(sort_by)} {pg.identifier(order)}', min_rating=min_rating)
    titles = [title['name'] for title in conn.columns]
    movies_dictionaries = []
    for i, movie in enumerate(movies):
        movies_dictionaries.append({title: movies[i][k] if title != 'cost' else float(movies[i][k]) for k, title in enumerate(titles)})
    if location is not None:
        available_movies = conn.run(f'SELECT DISTINCT movies.title FROM stock JOIN movies ON stock.movie_id = movies.movie_id JOIN stores ON stock.store_id = stores.store_id WHERE stores.city = {pg.literal(location)}')
        available_movies = [title for fake_list in available_movies for title in fake_list]
        return [movie for movie in movies_dictionaries if movie['title'] in available_movies]
    conn.close()
    return movies_dictionaries


def apply_discount_to_all_movies(percentage, save_database=False, table_name=None):
    if type(percentage) is not int:
        raise TypeError
    elif percentage > 90 or percentage <= 0:
        raise ValueError
    movies = get_movies()
    for movie in movies:
        movie['cost'] = movie['cost'] * (percentage/100)
    if save_database is True and table_name is not None:
        conn = pg.Connection(username, database=database)
        conn.run('START TRANSACTION')
        conn.run(f'DROP TABLE IF EXISTS sale_{pg.identifier(table_name)}; CREATE TABLE sale_{pg.identifier(table_name)} (movie_id SERIAL PRIMARY KEY, title VARCHAR,release_date DATE, rating INT, cost DECIMAL, classification VARCHAR)')
        for movie in movies:
            conn.run(f"INSERT INTO sale_{pg.identifier(table_name)} (title, release_date, rating, cost, classification) VALUES ({pg.literal(movie['title'])}, {pg.literal(movie['release_date'])}, {pg.literal(movie['rating'])}, {pg.literal(movie['cost'])}, {pg.literal(movie['classification'])})")
        conn.run('COMMIT')
        conn.close()
    return movies
