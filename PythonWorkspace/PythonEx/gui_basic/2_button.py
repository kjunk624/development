from tkinter import *
import tkinter

root = Tk()
root.title("Python_GUI")

btn1 = Button(root,text = "버튼 1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="버튼 2")
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼 3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼 4")
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="버튼 5")
btn5.pack()

photo = PhotoImage(file="gui_basic/image.png")
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print("버튼이 클릭 되었어요")
btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()

root.mainloop()
