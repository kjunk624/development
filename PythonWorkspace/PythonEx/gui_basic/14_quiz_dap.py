import os
from tkinter import *

root = Tk()
root.title("제목없음 - Windows 메모장")
root.geometry("640x480") # 가로 * 세로


# 열기, 저장 파일 이름
filename = "mynote.txt"

def open_file():
    # 화일이 있는지부터 확인
    if os.path.isfile(filename): # 화일 있으면 True, 없으면 False
        with open(filename,"r",encoding="utf8") as file:
            txt.delete("1.0",END)# 텍스트 위젯 본문 삭제
            txt.insert(END,file.read()) #file.read()한 내용을 txt에 넣는다

def save_file():
    with open(filename, "w", encoding="utf8") as file:
        file.write(txt.get("1.0",END)) # 모든 내용을 가져와 저장

menu = Menu(root)
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=open_file)
menu_file.add_command(label="저장", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=root.quit)
menu.add_cascade(label="파일", menu=menu_file)


#편집, 서식, 보기, 도움말
menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")

# 스크롤바
scrollbar = Scrollbar(root) # 다른 위젯이 없으므로 root에 직접 넣어 준다. 
scrollbar.pack(side="right", fill="y")


# 본문 영역
txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(fill="both", expand=True)
scrollbar.config(command=txt.yview) # 본문 영역과 맵핑

root.config(menu=menu)
root.mainloop()
