"""
    PyMySQL’s documentation
    https://pymysql.readthedocs.io/en/latest/index.html

    python3.8 -m pip install PyMySQL
"""

import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='phsn1788',
                             database='test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

with connection:

    # with connection.cursor() as cursor:
    #     # Create a new record
    #     sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
    #     cursor.execute(sql, ('william@python.org', 'william-dream'))
    #
    # # connection is not autocommit by default.
    # # So you must commit to save your changes.
    # connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('william@python.org',))
        result = cursor.fetchone()
        print(type(result))
        print(result)

    with connection.cursor() as cursor:
        sql = "select * from users"
        cursor.execute(sql)
        result = cursor.fetchmany(8)
        print(type(result))
        print(result)


if __name__ == '__main__':
    print("Hello PyMySQL")