import sqlite3
import prettytable

con = sqlite3.connect("movies.db")
cur = con.cursor()
sqlite_query = """
    DROP TABLE IF EXISTS user 
"""

def print_result(sqlite_query):
    """
    удаляем таблицу,
    тсозданную в ДЗ к уроку 19
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
