import sqlite3

def create_connection():
    connection = None
    try:
        connection = sqlite3.connect('databoase.db')
        print("Подлючение произошло успешно")
    except sqlite3.Error as e:
        print(f"Ошибка: {e}")
    return connection
def create_user(user_id: int,
                username: str,
                full_name: str)
    conn = create_connection()
    