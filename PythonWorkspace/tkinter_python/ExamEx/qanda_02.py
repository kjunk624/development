from tkinter import *
import sqlite3

root = Tk()
root.title('Question and Answer')
root.geometry("400x800")

# Create a database or connect to one
conn = sqlite3.connect('questions.db')
# Create cursor
cur = conn.cursor()

# Create table

cur.execute("""CREATE TABLE IF NOT EXISTS qna_data(
            question text,
            an1 text,
            an2 text,
            an3 text,
            an4 text,
            an5 text,
            corr integer
            )""")


def update():
    # Create a database or connect to one
    conn = sqlite3.connect('questions.db')
    # Create cursor
    cur = conn.cursor()

    record_id = delete_box.get()
    cur.execute("""UPDATE qna_data SET
        question = question,
        an1 = an1,
        an2 = an2,
        an3 = an3,
        an4 = an4,
        an5 = an5,
        corr = corr
        
        WHERE oid = :oid""",
                {
                    'question': question_editor.get(),
                    'an1': an1_editor.get(),
                    'an2': an2_editor.get(),
                    'an3': an3_editor.get(),
                    'an4': an4_editor.get(),
                    'an5': an5_editor.get(),
                    'corr': corr_editor.get(),
                    'oid': record_id
                })

    # Commit changes
    conn.commit()

    # Close Connection
    conn.close()

    editor.destroy()


# Create Edit Function to update a record
def edit():
    global editor
    editor = Tk()
    editor.title('Update A Record')
    editor.geometry("400x600")

    # Create a database or connect to one
    conn = sqlite3.connect('questions.db')
    # Create cursor
    cur = conn.cursor()

    record_id = delete_box.get()
    # Query the database
    cur.execute("SELECT * FROM qna_data WHERE oid= " + record_id)
    records = cur.fetchall()

    # query_label = Label(editor, text=print_records)
    # query_label.grid(row=12, column=0, columnspan=2)

    # Commit changes
    # conn.commit()
    #
    # # Close Connection
    # conn.close()

    # Create Global Variables for the text box names
    global question_editor
    global an1_editor
    global an2_editor
    global an3_editor
    global an4_editor
    global an5_editor
    global corr_editor

    # Create the Text Box
    question_editor = Entry(editor, width=30)
    question_editor.grid(row=0, column=1, padx=20)
    an1_editor = Entry(editor, width=30)
    an1_editor.grid(row=1, column=1, padx=20)
    an2_editor = Entry(editor, width=30)
    an2_editor.grid(row=2, column=1, padx=20)
    an3_editor = Entry(editor, width=30)
    an3_editor.grid(row=3, column=1, padx=20)
    an4_editor = Entry(editor, width=30)
    an4_editor.grid(row=4, column=1, padx=20)
    an5_editor = Entry(editor, width=30)
    an5_editor.grid(row=5, column=1, padx=20)
    corr_editor = Entry(editor, width=30)
    corr_editor.grid(row=6, column=1, padx=20)

    # Create Text Box Labels
    question_label = Label(editor, text="문제")
    question_label.grid(row=0, column=0)
    an1_label = Label(editor, text="문항1")
    an1_label.grid(row=1, column=0)
    an2_label = Label(editor, text="문랑2")
    an2_label.grid(row=2, column=0)
    an3_label = Label(editor, text="문항3")
    an3_label.grid(row=3, column=0)
    an4_label = Label(editor, text="문항4")
    an4_label.grid(row=4, column=0)
    an5_label = Label(editor, text="문항5")
    an5_label.grid(row=5, column=0)
    corr_label = Label(editor, text="정답")
    corr_label.grid(row=6, column=0)

    # loop through results
    for record in records:
        question_editor.insert(0, record[0])
        an1_editor.insert(0, record[1])
        an2_editor.insert(0, record[2])
        an3_editor.insert(0, record[3])
        an4_editor.insert(0, record[4])
        an5_editor.insert(0, record[5])
        corr_editor.insert(0, record[6])

    # Create a Save Button to Save the Record
    # edit_btn = Button(editor, text="저장 하기", command=update)
    # edit_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


# Create Function to Delete A Record
def delete():
    # Create a database or connect to one
    conn = sqlite3.connect('questions.db')
    # Create cursor
    cur = conn.cursor()

    # Delete a record
    cur.execute("DELETE FROM qna_data WHERE oid=" + delete_box.get())

    # Commit changes
    conn.commit()

    # Close Connection
    conn.close()


# Create Submit Function for database
def submit():
    # Create a database or connect to one
    conn = sqlite3.connect('questions.db')
    # Create cursor
    cur = conn.cursor()

    # Insert Into Table
    cur.execute("INSERT INTO qna_data VALUES (:question,:an1,:an2,:an3,:an4,:an5,:corr)",
                {
                    'question': question.get(),
                    'an1': an1.get(),
                    'an2': an2.get(),
                    'an3': an3.get(),
                    'an4': an4.get(),
                    'an5': an5.get(),
                    'corr': corr.get()
                })

    # Commit changes
    conn.commit()

    # Close Connection
    conn.close()

    question.delete(0, END)
    an1.delete(0, END)
    an2.delete(0, END)
    an3.delete(0, END)
    an4.delete(0, END)
    an5.delete(0, END)
    corr.delete(0, END)


# Create Query Function
def query():
    running = True
    while running:
        # Create a New windows for Questions
        global win
        win = Tk()
        win.title("Questions and Answers")
        win.geometry("480x640")

        # Create a database or connect to one
        conn = sqlite3.connect('questions.db')
        # Create cursor
        cur = conn.cursor()

        # Query the database
        cur.execute("SELECT oid,* FROM qna_data")
        records = cur.fetchall()
        global record
        for record in records:
            # record = cur.fetchone()

            print_records = " "
            # for record in records:
            print_records += str(record[0]) + ")" + str(record[1]) + "\n" + str(record[2]) \
                             + "\n" + str(record[3]) + "\n" + str(record[4]) + "\n" \
                             + str(record[5]) + "\n" + str(record[6]) + "\n"

            # query_label = Label(root, text=print_records)
            # query_label.grid(row=12, column=0, columnspan=2)

            query_label = Label(win, text=print_records)
            query_label.grid(row=0, column=0, columnspan=2)

            def enter_value(event):
                score = 0

                content = ent_ans.get()

                if str(content) == str(record[7]):
                    ans_label = Label(win, text="맞았습니다.^^")
                    ans_label.grid(row=9, column=1)
                    score += 1
                else:
                    ans_label = Label(win, text="틀렸습니다.ㅠㅠ")
                    ans_label.grid(row=9, column=1)

            # record += 1
            ent_ans = Entry(win, width=10)
            ent_ans.bind("<Return>", enter_value)
            ent_ans.grid(row=8, column=1, padx=10)

            ent_ans_label = Label(win, text="정답 ")
            ent_ans_label.grid(row=8, column=0)

        total_label = Label(win, text="문제 풀이 결과 당신은 " + str(len(records)) + "문제 중" + str(score) + "문제를 맞추었습니다.")
        total_label.grid(row=10, column=0)
        # "당신은 " + str(len(records)) + "문제 중" + str(score) + "문제를 맞추었습니다."

        # Commit changes
        conn.commit()

        # Close Connection
        conn.close()

        if record == len(records):
            running = False


# Create the Text Box
question = Entry(root, width=30)
question.grid(row=0, column=1, padx=20)
an1 = Entry(root, width=30)
an1.grid(row=1, column=1, padx=20)
an2 = Entry(root, width=30)
an2.grid(row=2, column=1, padx=20)
an3 = Entry(root, width=30)
an3.grid(row=3, column=1, padx=20)
an4 = Entry(root, width=30)
an4.grid(row=4, column=1, padx=20)
an5 = Entry(root, width=30)
an5.grid(row=5, column=1, padx=20)
corr = Entry(root, width=30)
corr.grid(row=6, column=1, padx=20)

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)

# Create Text Box Labels
question_label = Label(root, text="문제")
question_label.grid(row=0, column=0)
an1_label = Label(root, text="문항1")
an1_label.grid(row=1, column=0)
an2_label = Label(root, text="문랑2")
an2_label.grid(row=2, column=0)
an3_label = Label(root, text="문항3")
an3_label.grid(row=3, column=0)
an4_label = Label(root, text="문항4")
an4_label.grid(row=4, column=0)
an5_label = Label(root, text="문항5")
an5_label.grid(row=5, column=0)
corr_label = Label(root, text="정답")
corr_label.grid(row=6, column=0)

delete_box_label = Label(root, text="문제 번호 선택")
delete_box_label.grid(row=9, column=0, pady=5)

# Create Submit Button
submit_btn = Button(root, text="문제 만들기", command=submit)
submit_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a Save Button to Save the Record
edit_btn = Button(root, text="저장 하기", command=update)
edit_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a Query Button
query_btn = Button(root, text="문제 보이기", command=query)
query_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a Delete Button
delete_btn = Button(root, text="문제 지우기", command=delete)
delete_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create an Update Button
edit_btn = Button(root, text="수정 하기", command=edit)
edit_btn.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

root.mainloop()

# qna1 = Qnadata("다음 중 뼈를 이루는 구성이 아닌 것은?", "칼슘", "인", "골막", "골기", 4)
# qna2 = Qnadata("다음 중 신경계를 이루는 구성이 아닌 것은?", "시냅스", "축색돌기", "신경세포핵", "마이엘", 4)
#
# cur.execute("INSERT INTO qna_data VALUES(?,?,?,?,?,?)",
#             (qna1.question, qna1.an1, qna1.an2, qna1.an3, qna1.an4, qna1.corr))
# conn.commit()
#
# cur.execute("INSERT INTO qna_data VALUES(?,?,?,?,?,?)",
#             (qna2.question, qna2.an1, qna2.an2, qna2.an3, qna2.an4, qna2.corr))
# conn.commit()

# question_prompts = [
#     "다음 설명 중 틀린 것은? \n1)세포는 살아 있다.\n2)동물의 세포는 세포벽이 없다.\n3)세포는 유성생식을 통해 번식한다.\n4)세포는 핵을 가지고 있다.\n",
#     "다음 중 세포의 구성이 아닌 것은? \n1)세포핵\n2)골기체\n3)미톤콘드리아\n4)마이봄선\n\n",
#     "다음 중 혈액 구성이 아닌 것은? \n1)모양체\n2)호중구\n3)혈소판\n4)적혈구\n\n"
# ]
#
# questions = [
#     Question(question_prompts[0], "3"),
#     Question(question_prompts[1], "4"),
#     Question(question_prompts[2], "1")
# ]


# def run_test(questions):
#     score = 0
#     for question in questions:
#         answer = input(question.prompt)
#         if answer == question.answer:
#             score += 1
#     print("당신은 " + str(len(questions)) + "문제 중" + str(score) + "문제를 맞추었습니다.")
#     # "당신은 " + str(len(questions)) + "문제 중" + str(score) + "문제를 맞추었습니다."


# run_test(questions)