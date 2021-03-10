from tkinter import *
import sqlite3
import makemydata

class MakeInsertData:
    # Insert Into Table
    def __init__(self, root):
        self.conn = sqlite3.connect('questions.db')
        self.cur = self.conn.cursor
        self.cur.execute("INSERT INTO qna_data VALUES (:question,:an1,:an2,:an3,:an4,:an5,:corr)",
                    {
                        'question': self.question.get(),
                        'an1': self.an1.get(),
                        'an2': self.an2.get(),
                        'an3': self.an3.get(),
                        'an4': self.an4.get(),
                        'an5': self.an5.get(),
                        'corr': self.corr.get()
                    })

        self.stop_btn = Button(root, text="입력 끝", command=root.quit, font=("맑은고딕", 10))
        self.stop_btn.grid(row=7, column=0, padx=50, pady=50)
        self.stop_btn.place(relx=0.4, rely=0.8, anchor=CENTER)
        self.go_on_btn = Button(root, text="다음 문제 입력", command=root.submit, font=("맑은고딕", 10))
        self.go_on_btn.grid(row=7, column=1, pady=50)
        self.go_on_btn.place(relx=0.5, rely=0.8, anchor=CENTER)

        # Commit changes
        self.conn.commit()

        # Close Connection
        self.conn.close()
