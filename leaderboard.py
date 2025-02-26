from db import get_db_connection


def get_top_users():
    """Fetch the top 3 users with the highest scores."""
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        query = """
        SELECT users.username, score.points
        FROM score
        JOIN users ON score.user_id = users.user_id
        ORDER BY score.points DESC
        LIMIT 3;
        """
        cursor.execute(query)
        top_users = cursor.fetchall()

        return top_users  # Returns list of tuples (username, points)

    except Exception as error:
        print(f"Error fetching leaderboard: {error}")
        return []  # Return empty list if error occurs
    finally:
        if connection:
            cursor.close()
            connection.close()
