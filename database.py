import sqlite3


def check_existing_user(username):  # check if username already exists
    with sqlite3.connect('proj4.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM users WHERE username=?", [username])
        return cursor.fetchone()[0]


def create_user(username, password):  # create new user
    with sqlite3.connect('proj4.db') as connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO users VALUES (?, ?)", [username, password])


def login_user(username, password):  # check that user with given username and password exists
    with sqlite3.connect('proj4.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM users WHERE username=? AND password=?", [username, password])
        return cursor.fetchone()[0]


def insert_book(isbn, title, author, published, description):
    with sqlite3.connect('proj4.db') as connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO books VALUES (?, ?, ?, ?, ?)", [isbn, title, author, published, description])


def insert_game(title, publisher, developer, release, description):
    with sqlite3.connect('proj4.db') as connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO games VALUES (?, ?, ?, ?, ?, ?)", [None, title, publisher, developer, release, description])


def insert_movie(title, director, release, description):
    with sqlite3.connect('proj4.db') as connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO movies VALUES (?, ?, ?, ?, ?)", [None, title, director, release, description])


def get_books(page):
    with sqlite3.connect('proj4.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM books")
        return cursor.fetchall()[page * 4 - 4:page * 4]


def get_books_count():
    with sqlite3.connect('proj4.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM books")
        return cursor.fetchone()[0]


def get_games(page):
    with sqlite3.connect('proj4.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM games")
        return cursor.fetchall()[page * 4 - 4:page * 4]


def get_games_count():
    with sqlite3.connect('proj4.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM games")
        return cursor.fetchone()[0]


def get_movies(page):
    with sqlite3.connect('proj4.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM movies")
        return cursor.fetchall()[page * 4 - 4:page * 4]


def get_movies_count():
    with sqlite3.connect('proj4.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM movies")
        return cursor.fetchone()[0]


def check_book_already_added(username, isbn):
    with sqlite3.connect('proj4.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM userbooks WHERE username=? AND isbn=?", [username, isbn])
        return cursor.fetchone()[0]


def check_game_already_added(username, gid):
    with sqlite3.connect('proj4.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM usergames WHERE username=? AND gid=?", [username, gid])
        return cursor.fetchone()[0]


def check_movie_already_added(username, mid):
    with sqlite3.connect('proj4.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM usermovies WHERE username=? AND mid=?", [username, mid])
        return cursor.fetchone()[0]


# insert queries for usergames, books, movies
def insert_user_game(username, gid):
    with sqlite3.connect('proj4.db') as connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO usergames VALUES(?,?,?)", [username, gid, 0])


def insert_user_movie(username, mid):
    with sqlite3.connect('proj4.db') as connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO usermovies VALUES(?,?,?)", [username, mid, 0])


def insert_user_book(username, isbn):
    with sqlite3.connect('proj4.db') as connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO userbooks VALUES(?,?,?)", [username, isbn, 0])


def update_user_book_rating(username, isbn, rating):
    with sqlite3.connect('proj4.db') as connection:
        cursor = connection.cursor()
        cursor.execute("UPDATE userbooks SET rating=? WHERE username=? AND isbn=?", [rating, username, isbn])


def update_user_game_rating(username, gid, rating):
    with sqlite3.connect('proj4.db') as connection:
        cursor = connection.cursor()
        cursor.execute("UPDATE usergames SET rating=? WHERE username=? AND gid=?", [rating, username, gid])


def update_user_movie_rating(username, mid, rating):
    with sqlite3.connect('proj4.db') as connection:
        cursor = connection.cursor()
        cursor.execute("UPDATE usermovies SET rating=? WHERE username=? AND mid=?", [rating, username, mid])


# delete an entity from their specified cat collection
def delete_user_game(username, gid):
    with sqlite3.connect('proj4.db') as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM usergames WHERE username=? AND gid=?", [username, gid])


def delete_user_movie(username, mid):
    with sqlite3.connect('proj4.db') as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM usermovies WHERE username=? AND mid=?", [username, mid])


def delete_user_book(username, isbn):
    with sqlite3.connect('proj4.db') as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM userbooks WHERE username=? AND isbn=?", [username, isbn])


# search queries/by movie titles/game title/ isbn/book title
def search_books(search, page):
    with sqlite3.connect('proj4.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM books WHERE btitle LIKE ? OR isbn LIKE ?", ['%' + search + '%', '%' + search + '%'])
        return cursor.fetchall()[page * 4 - 4: page * 4], len(cursor.fetchall())


def search_games(search, page):
    with sqlite3.connect('proj4.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM games WHERE gtitle LIKE ?", ['%' + search + '%'])
        return cursor.fetchall()[page * 4 - 4: page * 4], len(cursor.fetchall())


def search_movies(search, page):
    with sqlite3.connect('proj4.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM movies WHERE mtitle LIKE ?", ['%' + search + '%'])
        return cursor.fetchall()[page * 4 - 4: page * 4], len(cursor.fetchall())


# collection filtered by cat of movie/game/books to display titles to user of their collection ordered by rating
def get_user_games(username, page):
    with sqlite3.connect('proj4.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT games.gid, games.gtitle, games.publisher, games.developer, games.grelease, games.gdescription, usergames.rating FROM games, usergames WHERE games.gid=usergames.gid AND usergames.username=?", [username])
        return cursor.fetchall()[page * 4 - 4:page * 4]


def get_user_movies(username, page):
    with sqlite3.connect('proj4.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT movies.mid, movies.mtitle, movies.director, movies.mrelease, movies.mdescription, usermovies.rating FROM movies, usermovies WHERE movies.mid=usermovies.mid AND usermovies.username=?", [username])
        return cursor.fetchall()[page * 4 - 4:page * 4]


def get_user_books(username, page):
    with sqlite3.connect('proj4.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT books.isbn, books.btitle, books.author, books.published, books.bdescription, userbooks.rating FROM books, userbooks WHERE books.isbn=userbooks.isbn AND userbooks.username=?", [username])
        return cursor.fetchall()[page * 4 - 4:page * 4]


# count total media collection by three cat and altogether
def get_user_books_count(username):
    with sqlite3.connect('proj4.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM userbooks WHERE username=?", [username])
        return cursor.fetchone()[0]


def get_user_games_count(username):
    with sqlite3.connect('proj4.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM usergames WHERE username=?", [username])
        return cursor.fetchone()[0]


def get_user_movies_count(username):
    with sqlite3.connect('proj4.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM usermovies WHERE username=?", [username])
        return cursor.fetchone()[0]

