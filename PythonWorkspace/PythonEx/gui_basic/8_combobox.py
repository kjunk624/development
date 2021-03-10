import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Python_GUI")
root.geometry("640x480")

values = [str(i) + "일" for i in range(1,32)] # 1 ~ 31 까지의 숫자
combobox = ttk.Combobox(root, height=5, values=values) # 항목이 5개만 나타남
combobox.pack()
combobox.set("카드결제일") # 최초 목록 제목 설정

readonly_combobox = ttk.Combobox(root, height=10, values=values,state="readonly")
readonly_combobox.current(0) # 0번쩨 인덱스 값 선택
readonly_combobox.pack()

def btncmd():
    print(combobox.get()) # 선택된 값 표시
    print(readonly_combobox.get())
    
   
btn = Button(root,text="선택", command=btncmd)
btn.pack()



root.mainloop()