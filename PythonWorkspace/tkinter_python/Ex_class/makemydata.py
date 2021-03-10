import sqlite3
class MakeMyData:
    def __init__(self, root):
        # Create a database or connect to one
        self.conn = sqlite3.connect('questions.db')
        # Create cursor
        self.cur = self.conn.cursor()

        # Create table

        self.cur.execute("""CREATE TABLE IF NOT EXISTS qna_data(
                    question text,
                    an1 text,
                    an2 text,
                    an3 text,
                    an4 text,
                    an5 text,
                    corr integer
                    )""")
        self.conn.commit()
        self.conn.close()
