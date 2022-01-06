import sqlite3

if __name__ == '__main__':
    connection = sqlite3.connect('proj4.db')
    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS
    users(
        username TEXT PRIMARY KEY,
        password TEXT NOT NULL
    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS
    books(
        isbn TEXT PRIMARY KEY,
        btitle TEXT,
        author TEXT,
        published TEXT,
        bdescription TEXT
    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS
    games(
        gid INTEGER PRIMARY KEY,
        gtitle TEXT,
        publisher TEXT,
        developer TEXT,
        grelease TEXT,
        gdescription TEXT
    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS
    movies(
        mid INTEGER PRIMARY KEY,
        mtitle TEXT,
        director TEXT,
        mrelease TEXT,
        mdescription TEXT
    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS
    userbooks(
        username TEXT,
        isbn TEXT,
        rating INTEGER,
        FOREIGN KEY(username) REFERENCES users(username),
        FOREIGN KEY(isbn) REFERENCES books(isbn)
    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS
    usergames(
        username TEXT,
        gid INTEGER,
        rating INTEGER,
        PRIMARY KEY (username, gid)
        FOREIGN KEY(username) REFERENCES users(username),
        FOREIGN KEY(gid) REFERENCES games(gid)
    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS
    usermovies(
        username TEXT,
        mid INTEGER,
        rating INTEGER,
        PRIMARY KEY (username, mid)
        FOREIGN KEY(username) REFERENCES users(username),
        FOREIGN KEY(mid) REFERENCES movies(mid)
    )""")

    cursor.close()

