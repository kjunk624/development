from tkinter import *
# 1.타이틀 제목
root = Tk()
root.title("제목 없음")
root.geometry("640x480")

# 스트롤바 만들기
frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

#listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set)
txt_box = Listbox(frame, selectmode="extended", height="400", yscrollcommand=scrollbar.set)
# 텍스트 창 만들기


label = Label(root, text="")
label.pack()


# 3. 실제 메뉴 구현
def open_file():
    with open('mynot.txt','r')as f:
        lines= f.readline()
        for line in lines:
            print(lines)

        

def save_file():
    with open('mynot.txt','w')as f:
        f.write("test")
        f.write("ok?")

def quit():
    exit()


# 2.메뉴 만들기
menu = Menu(root)

menu_file = Menu(menu,tearoff=0)
menu_file.add_command(label="열기", command=open_file)
menu_file.add_command(label="저장", command=save_file)
menu_file.add_command(label="끝내기", command=quit)

menu.add_cascade(label="파일",menu=menu_file)

menu_edit = Menu(menu, tearoff=0)
menu.add_cascade(label="편집",menu=menu_edit)
menu_form = Menu(menu, tearoff=0)
menu.add_cascade(label="서식",menu=menu_form)
menu_view = Menu(menu, tearoff=0)
menu.add_cascade(label="보기",menu=menu_view)
menu_help = Menu(menu, tearoff=0)
menu.add_cascade(label="도움말",menu=menu_help)



root.config(menu=menu)
root.mainloop()