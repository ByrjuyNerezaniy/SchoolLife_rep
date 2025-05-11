import sqlite3

# Создание базы данных и таблицы для сообщений
def create_db():
    conn = sqlite3.connect('chat.db')
    c = conn.cursor()
    # Создаем таблицу для хранения сообщений
    c.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id TEXT NOT NULL,
            user TEXT NOT NULL,
            message TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

create_db()