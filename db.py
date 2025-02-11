import psycopg2


def get_db_connection():
    return psycopg2.connect(
        dbname="sQuiz_game",
        user="postgres",
        password="123",
        host="localhost",
        port="5432"
    )


def execute_query(query, params=None, fetch=False):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(query, params)
        if fetch:
            return cursor.fetchall()
        connection.commit()
    except Exception as error:
        print(f"Error: {error}")
    finally:
        if connection:
            cursor.close()
            connection.close()
