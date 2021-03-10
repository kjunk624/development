from tkinter import *

root = Tk()
root.title("Python_GUI")
root.geometry("640x480")

label1 = Label(root, text="안녕하세요?")
label1.pack()

photo = PhotoImage(file="gui_basic/image.png")
label2 = Label(root, image=photo)
label2.pack()


def change():
    label1.config(text="또만나요")

    global photo2 # 함수내에서 label을 바꾸려 항때 전역 변수로 설정하지 않으면 가비지 컬렉터에 의해 변수가 없어짐
    photo2 = PhotoImage(file="gui_basic/image2.png")
    label2.config(image=photo2)

btn = Button(root, text="클릭", command=change)
btn.pack()

root.mainloop()