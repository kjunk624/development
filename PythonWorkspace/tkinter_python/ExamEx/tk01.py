from tkinter import *
from datetime import datetime

win = Tk()
win.title("Q and A")
win.geometry("640x480")
win.option_add("*Font", "궁서 20")


def alert():
    dnow = datetime.now()
    btn1.config(text=dnow)


# 버튼
btn1 = Button(win)
btn1.config(width=20, height=2)
btn1.config(text="현재 시간")
btn1.config(command=alert)
btn1.pack()

# 라밸
lab1 = Label(win)
lab1.config(text="Question")
lab1.pack()

win.mainloop()
