from tkinter import *

root = Tk()
root.title("Python_GUI")
root.geometry("640x480")

txt = Text(root, width=30, height=5) # 텍스트 필드르 만듦
txt.pack()

txt.insert(END, "글자를 입력하세요") # 미리 입력된 글자(힌트 텍스트)


e = Entry(root, width=30)
e.pack()
e.insert(0, "한줄만 입력해요") # 줄바꿈 안됨


def btncmd():

    # 내용 출력
    print(txt.get("1.0", END)) # 1: 첫번째 라인, 0 : 0번째 column위치
    print(e.get()) # Entry내용 가져오기

    
    # 내용 삭제
    txt.delete("1.0",END)
    e.delete(0,END)

btn = Button(root,text="클릭", command=btncmd)
btn.pack()

root.mainloop()