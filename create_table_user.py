import sqlite3
import prettytable

con = sqlite3.connect("movies.db")
cur = con.cursor()
sqlite_query = """
    CREATE TABLE user (
        Id integer PRIMARY KEY AUTOINCREMENT, 
        Email varchar(255) NOT NULL, 
        Password varchar(255),
        Name varchar(255),
        Surname varchar(255),
        Favorite_genre integer
    )
"""

def print_result(sqlite_query):
    """
    создаю таблицу в базе вручную,
    так как через модели не создалось
    :param sqlite_query:
    :return:
    """
    cur.execute(sqlite_query)
    result_query = ('SELECT * from user')
    table = cur.execute(result_query)
    mytable = prettytable.from_db_cursor(table)
    mytable.max_width = 30
    print(mytable)


if __name__ == '__main__':
    print_result(sqlite_query)
