import sqlite3
 
class DB_Controller:
    conn: sqlite3.Connection
    cursor: sqlite3.Cursor
 
    def __init__(self, db_name) -> None:
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
   
    def init_table(self):
        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS question (id INTEGER PRIMARY KEY AUTOINCREMENT,
           question TEXT, max_score INTEGER, correct_answer TEXT, incorrect_answer TEXT)''')
   
    def init_data(self):
        data = [
            ("Як звати?", 2, "Денис", "Мікаель"),
            ("Який зараз рік?", 3, "2024", "1924"),
            ("Скільки у людини хромосом?", 10, "46", "47")
        ]
        self.cursor.executemany(
            '''INSERT INTO question (question, max_score, correct_answer,
           incorrect_answer) VALUES (?, ?, ?, ?)''', data
            )
        self.conn.commit()
 
    def get_data(self):
        self.cursor.execute(
            '''SELECT question, max_score FROM question'''
            )
        data = self.cursor.fetchall()
        print(data)
 
    def close(self):
        self.cursor.close()
        self.conn.close()
 
db = DB_Controller('question.db')
 
# db.init_table() 
# db.init_data()
db.get_data()
db.close()