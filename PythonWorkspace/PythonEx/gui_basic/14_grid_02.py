import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("Python_GUI")
root.geometry("640x480")

# btn1 = Button(root, text="버튼1")
# btn2 = Button(root, text="버튼2")

# # btn1.pack()
# # btn2.pack()

# # btn1.pack(side="left")
# # btn2.pack(side="right")

# btn1.grid(row=0, column=0)
# btn2.grid(row=1, column=1)

# 맨윗줄
btn_f16 = Button(root,text="F16")
btn_f17 = Button(root,text="F17")
btn_f18 = Button(root,text="F18")
btn_f19 = Button(root,text="F19")

btn_f16.grid(row=0, column="0", sticky=N+E+W+S)
btn_f17.grid(row=0, column="1", sticky=N+E+W+S)
btn_f18.grid(row=0, column="2", sticky=N+E+W+S)
btn_f19.grid(row=0, column="3", sticky=N+E+W+S)

# clear줄
btn_clear = Button(root, text="clear")
btn_equal = Button(root, text="=")
btn_div = Button(root, text="/")
btn_mul = Button(root, text="*")

btn_clear.grid(row=1, column="0", sticky=N+E+W+S)
btn_equal.grid(row=1, column="1", sticky=N+E+W+S)
btn_div.grid(row=1, column="2", sticky=N+E+W+S)
btn_mul.grid(row=1, column="3", sticky=N+E+W+S)

# 7시작 줄

btn_7 = Button(root, text="7")
btn_8 = Button(root, text="8")
btn_9 = Button(root, text="9")
btn_sub = Button(root, text="-")

btn_7.grid(row=2, column="0", sticky=N+E+W+S)
btn_8.grid(row=2, column="1", sticky=N+E+W+S)
btn_9.grid(row=2, column="2", sticky=N+E+W+S)
btn_sub.grid(row=2, column="3", sticky=N+E+W+S)

# 4 시작줄

btn_4 = Button(root, text="4")
btn_5 = Button(root, text="5")
btn_6 = Button(root, text="6")
btn_plus = Button(root, text="plus")

btn_4.grid(row=3, column="0", sticky=N+E+W+S)
btn_5.grid(row=3, column="1", sticky=N+E+W+S)
btn_6.grid(row=3, column="2", sticky=N+E+W+S)
btn_plus.grid(row=3, column="3", sticky=N+E+W+S)

# 1 시작줄

btn_1 = Button(root, text="1")
btn_2 = Button(root, text="2")
btn_3 = Button(root, text="3")
btn_enter = Button(root, text="enter")  #  세로로 합쳐짐

btn_1.grid(row=4, column="0", sticky=N+E+W+S)
btn_2.grid(row=4, column="1", sticky=N+E+W+S)
btn_3.grid(row=4, column="2", sticky=N+E+W+S)
btn_enter.grid(row=4, column="3", rowspan=2, sticky=N+E+W+S) # 현재 위치로 부터 아래쪽으로 몇줄을 더함
# 0 줄

btn_0 = Button(root, text="0")
btn_point = Button(root, text=".")

btn_0.grid(row=5, column="0",columnspan=2, sticky=N+E+W+S) # 현재 위치로 부터 오른 쪽으로 몇칸 더함
btn_point.grid(row=5, column="2", sticky=N+E+W+S)


root.mainloop()