from tkinter import *
from tkinter import Menu, messagebox, Label
import sqlite3

root = Tk()
root.title("시험 문제 풀이 연습")
width_value = root.winfo_screenwidth()
height_value = root.winfo_screenheight()
# root.geometry("%dx%d+0+0" % (width_value, height_value))
# root.geometry("{}x{}+0+0".format(width_value, height_value))
root.geometry(f"{width_value}x{height_value}+0+0")

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
conn.commit()
conn.close()


# Create Submit Function for database
def submit():
    mk_question_btn.destroy()
    question_btn.destroy()
    # delete_box_label.destroy()
    # delete_box.destroy()
    delete_btn.destroy()
    edit_btn.destroy()
    # Create a database or connect to one
    conn = sqlite3.connect('questions.db')
    # Create cursor
    cur = conn.cursor()

    # Create the Text Box
    question = Entry(root, width=70, font=("맑은고딕", 15))
    question.grid(row=0, column=1, padx=20, pady=40)
    an1 = Entry(root, width=70, font=("맑은고딕", 15))
    an1.grid(row=1, column=1, padx=20)
    an2 = Entry(root, width=70, font=("맑은고딕", 15))
    an2.grid(row=2, column=1, padx=20)
    an3 = Entry(root, width=70, font=("맑은고딕", 15))
    an3.grid(row=3, column=1, padx=20)
    an4 = Entry(root, width=70, font=("맑은고딕", 15))
    an4.grid(row=4, column=1, padx=20)
    an5 = Entry(root, width=70, font=("맑은고딕", 15))
    an5.grid(row=5, column=1, padx=20)
    corr = Entry(root, width=70, font=("맑은고딕", 15))
    corr.grid(row=6, column=1, padx=20)

    # delete_box = Entry(root, width=30)
    # delete_box.grid(row=9, column=1, pady=5)

    # Create Text Box Labels
    question_label = Label(root, text="문 제", font=("맑은고딕", 15))
    question_label.grid(row=0, column=0, pady=40)
    an1_label = Label(root, text="문항1", font=("맑은고딕", 15))
    an1_label.grid(row=1, column=0)
    an2_label = Label(root, text="문항2", font=("맑은고딕", 15))
    an2_label.grid(row=2, column=0)
    an3_label = Label(root, text="문항3", font=("맑은고딕", 15))
    an3_label.grid(row=3, column=0)
    an4_label = Label(root, text="문항4", font=("맑은고딕", 15))
    an4_label.grid(row=4, column=0)
    an5_label = Label(root, text="문항5", font=("맑은고딕", 15))
    an5_label.grid(row=5, column=0)
    corr_label = Label(root, text="정 답", font=("맑은고딕", 15))
    corr_label.grid(row=6, column=0)

    question.focus()

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

    stop_btn = Button(root, text="입력 끝", command=root.quit, font=("맑은고딕", 10))
    stop_btn.grid(row=7, column=0, padx=50, pady=50)
    stop_btn.place(relx=0.4, rely=0.8, anchor=CENTER)
    go_on_btn = Button(root, text="다음 문제 입력", command=submit, font=("맑은고딕", 10))
    go_on_btn.grid(row=7, column=1, pady=50)
    go_on_btn.place(relx=0.5, rely=0.8, anchor=CENTER)

    # Commit changes
    conn.commit()

    # Close Connection
    conn.close()


# Create Query Function
def query():
    mk_question_btn.destroy()
    question_btn.destroy()
    delete_box_label.destroy()
    delete_box.destroy()
    delete_btn.destroy()
    edit_btn.destroy()

    # Create a New windows for Questions
    # win = Tk()
    # win.title("Questions and Answers")
    # win.geometry("480x640")

    # Create a database or connect to one
    conn = sqlite3.connect('questions.db')
    # Create cursor
    cur = conn.cursor()

    # Query the database
    cur.execute("SELECT oid,* FROM qna_data")
    records = cur.fetchall()

    # global record
    global print_records
    global query_label
    global record
    global score

    """ ======= 아래부터 아들이 수정한 내용 =========
    for 문으로도 방법이 있을텐데 일단 재귀함수 형식으로 썼어요
    ask_question이라는 함수가 for문 안의 일을 다 고대로 처리하는데 db안에 이번에 처리할 질문 번호랑 
    남은 질문개수를 계속 트래킹해요. 
    1. 일단 남은 질문 개수가 0 이하면 그냥 종료.
    2. 전체 질문 리스트인 records에서 이번 질문 번호인 question_idx 번재 질문을 꺼내서 record에 저장
    3. next_question_id에 다음 질문번호 저장(1증가), now_remain_question에 이제 남은 질문 개수 저장(1감소)
    4. 쭉 동일하다가 next question 수정했습니다.
    5. next question도 마찬가지로 record, 질문 번호, 남은 질문 개수를 변수로 받아요
    6. delete, forget으로 화면 클리어해주고 ask_question 새로 진행, 그런데 이번엔 다음번 질문과 적어진 잔여 질문개수로
    7. next_question 함수의 수정사항을 반영하기 위해 next_btn 에서 command를 lambda 함수로 썼어요. 그렇게 해야지만 command= 옆에 들어갈 함수에 변수를 제공할 수 있어서  
    8. 마지막 def 끝나고 실제 ask_question 한번 실행하면 재귀식으로 진행

    실행해보니까 잘되는데 gui에 쏴주는 과정에서 문제 번호가 뒤로갈수록 오른쪽으로 치우쳐서 보여지는 문제가 있네요.
    """
    num_record = len(records)
    remain_question = num_record
    question_idx = 0

    def ask_question(records, question_idx, remain_question):
        if remain_question <= 0:
            response = messagebox.showinfo("문제 종료", "더이상 문제가 없습니다.")
            total_label = Label(root,
                                text="문제 풀이 결과 당신은 " + str(num_record) + "문제 중" +str(remain_question)  + "문제를 맞추었습니다.")
            total_label.grid(row=10, column=0)
            return
        record = records[question_idx]
        next_question_idx = question_idx + 1
        now_remain_question = remain_question - 1
        print_records = ''
        print_records += str(record[0]) + "." + str(record[1]) + "\n" + " (1)" + str(record[2]) \
                         + "\n" + " (2)" + str(record[3]) + "\n" + " (3)" + str(record[4]) + "\n" \
                         + " (4)" + str(record[5]) + "\n" + " (5)" + str(record[6]) + "\n"

        # print(print_records)

        query_label = Label(root, text=print_records, justify="left", font=("나눔명조체", 18))
        query_label.grid(row=0, column=0, columnspan=2)

        # Entry value for correct answer
        global content
        # global ans_label
        # global score

        def enter_value(event):
            global ans_label
            score = 0
            content = ent_ans.get()
            if str(content) == str(record[7]):
                ans_label = Label(root, text="맞았습니다.^^", font=("맑은고딕", 10))
                ans_label.grid(row=9, column=0)
                score += 1
            else:
                ans_label = Label(root, text="틀렸습니다.ㅠㅠ", font=("맑은고딕", 10))
                ans_label.grid(row=9, column=0)
            # total_label = Label(win,
            #                     text="문제 풀이 결과 당신은 " + str(len(question_idx)) + "문제 중" + str(score) + "문제를 맞추었습니다.")
            # total_label.grid(row=10, column=0)

        # Create Button for next question
        def next_question(records, question_idx, remain_question):
            global ans_label
            ent_ans.delete(0, "end")
            ans_label.grid_forget()
            query_label.grid_forget()
            ask_question(records, question_idx, remain_question)

        ent_ans_label = Label(root, text="정답 ", font=("맑은고딕", 10))
        ent_ans_label.grid(row=8, column=0)

        ent_ans = Entry(root, width=10)
        ent_ans.focus_set()
        ent_ans.bind("<Return>", enter_value)
        ent_ans.grid(row=8, column=1, padx=10)

        next_btn = Button(root, text="다음 문제",
                          command=lambda: next_question(records, next_question_idx, now_remain_question),
                          font=("맑은고딕", 10))
        next_btn.grid(row=9, column=1)

        # total_label = Label(root, text="문제 풀이 결과 당신은 " + str(len(question_idx)) + "문제 중" + str(score) + "문제를 맞추었습니다.")
        # total_label.grid(row=10, column=0)

    ask_question(records, question_idx, remain_question)

    # total_label = Label(win, text="문제 풀이 결과 당신은 " + str(len(question_idx)) + "문제 중" + str(score) + "문제를 맞추었습니다.")
    # total_label.grid(row=10, column=0)

    # Commit changes
    conn.commit()

    # Close Connection
    conn.close()


# Create Function to Delete A Record
def delete():
    global record
    global delete_box
    global delete_box_label
    global delete_btn
    global edit_btn

    mk_question_btn.destroy()
    question_btn.destroy()
    delete_btn.destroy()
    edit_btn.destroy()

    # Create a database or connect to one
    conn = sqlite3.connect('questions.db')
    # Create cursor
    cur = conn.cursor()

    # Delete a record
    cur.execute("DELETE FROM qna_data WHERE oid=" + delete_box.get())
    delete_box.delete(0, END)
    response = messagebox.showinfo("문제 삭제", "선택된 문제가 삭제되었습니다.")

    # Commit changes
    conn.commit()

    # Close Connection
    conn.close()


def update():
    # Create a database or connect to one
    conn = sqlite3.connect('questions.db')
    # Create cursor
    cur = conn.cursor()

    record_id = delete_box.get()
    cur.execute("""UPDATE qna_data SET
        question = :question,
        an1 = :an1,
        an2 = :an2,
        an3 = :an3,
        an4 = :an4,
        an5 = :an5,
        corr = :corr

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

    # editor.destroy()


# Create Edit Function to update a record
def edit():
    mk_question_btn.destroy()
    question_btn.destroy()
    delete_btn.destroy()
    edit_btn.grid_forget()

    # Create a database or connect to one
    conn = sqlite3.connect('questions.db')
    # Create cursor
    cur = conn.cursor()

    record_id = delete_box.get()
    # Query the database
    cur.execute("SELECT * FROM qna_data WHERE oid= " + record_id)
    records = cur.fetchall()

    # Create Global Variables for the text box names
    global question_editor
    global an1_editor
    global an2_editor
    global an3_editor
    global an4_editor
    global an5_editor
    global corr_editor

    # Create the Text Box
    question_editor = Entry(root, width=70, font=("맑은고딕", 15))
    question_editor.grid(row=0, column=1, padx=20, pady=40)
    an1_editor = Entry(root, width=70, font=("맑은고딕", 15))
    an1_editor.grid(row=1, column=1, padx=20, pady=5)
    an2_editor = Entry(root, width=70, font=("맑은고딕", 15))
    an2_editor.grid(row=2, column=1, padx=20, pady=5)
    an3_editor = Entry(root, width=70, font=("맑은고딕", 15))
    an3_editor.grid(row=3, column=1, padx=20, pady=5)
    an4_editor = Entry(root, width=70, font=("맑은고딕", 15))
    an4_editor.grid(row=4, column=1, padx=20, pady=5)
    an5_editor = Entry(root, width=70, font=("맑은고딕", 15))
    an5_editor.grid(row=5, column=1, padx=20, pady=5)
    corr_editor = Entry(root, width=70, font=("맑은고딕", 15))
    corr_editor.grid(row=6, column=1, padx=20, pady=5)

    # Create Text Box Labels
    question_label = Label(root, text="문 제", font=("맑은고딕", 15))
    question_label.grid(row=0, column=0)
    an1_label = Label(root, text="문항1", font=("맑은고딕", 15))
    an1_label.grid(row=1, column=0)
    an2_label = Label(root, text="문항2", font=("맑은고딕", 15))
    an2_label.grid(row=2, column=0)
    an3_label = Label(root, text="문항3", font=("맑은고딕", 15))
    an3_label.grid(row=3, column=0)
    an4_label = Label(root, text="문항4", font=("맑은고딕", 15))
    an4_label.grid(row=4, column=0)
    an5_label = Label(root, text="문항5", font=("맑은고딕", 15))
    an5_label.grid(row=5, column=0)
    corr_label = Label(root, text="정 답", font=("맑은고딕", 15))
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
    save_btn = Button(root, text="저장 하기", command=update, font=("맑은고딕", 10))
    save_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    conn.commit()
    conn.close()


# 메뉴바 만들기
menubar = Menu(root)

menu1 = Menu(menubar, tearoff=0)
menu2 = Menu(menubar, tearoff=0)
menu1.add_command(label="문제 만들기", command=submit)
menu1.add_command(label="문제 풀기", command=query)
menu2.add_command(label="문제 지우기", command=delete)
menu2.add_command(label="문제 수정하기", command=edit)

menu1.add_separator()
menu1.add_command(label="끝내기", command=root.quit)
menubar.add_cascade(label="File", menu=menu1)
menubar.add_cascade(label="Edit", menu=menu2)

root.config(menu=menubar)

mk_question_btn = Button(root, text="문제 만들기", command=submit, padx=100, font=("맑은고딕", 15))
mk_question_btn.grid(row=0, column=0, pady=150)
mk_question_btn.place(relx=0.5, rely=0.1, anchor=CENTER)

question_btn = Button(root, text="문제 풀기", command=query, padx=105, font=("맑은고딕", 15))
question_btn.grid(row=1, column=0, pady=20)
question_btn.place(relx=0.5, rely=0.3, anchor=CENTER)

# Create a Delete Button
delete_btn = Button(root, text="문제 지우기", command=delete, padx=100, font=("맑은고딕", 15))
delete_btn.grid(row=2, column=0, pady=20)
delete_btn.place(relx=0.5, rely=0.5, anchor=CENTER)

# Create an Update Button
edit_btn = Button(root, text="수정 하기", command=edit, padx=105, font=("맑은고딕", 15))
edit_btn.grid(row=3, column=0, pady=20)
edit_btn.place(relx=0.5, rely=0.7, anchor=CENTER)

delete_box_label = Label(root, text="편집할 문제 번호 선택", font=("맑은고딕", 13))
delete_box_label.grid(row=13, column=0, padx=10)

delete_box = Entry(root, width=10, font=("맑은고딕", 13))
delete_box.grid(row=13, column=1, padx=50)
delete_box.focus()

root.mainloop()
