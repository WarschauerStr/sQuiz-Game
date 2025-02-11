from db import get_db_connection


def get_top_users():
    """fetch and display top 3 users with the highest scores"""
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

        if not top_users:
            print("\n🏆 No scores available yet.")
            return

        print("\n🏆 Top 3 Players 🏆")
        for idx, (username, points) in enumerate(top_users, 1):
            print(f"{idx}. {username} - {points} points")

    except Exception as error:
        print(f"error: {error}")
    finally:
        if connection:
            cursor.close()
            connection.close()
