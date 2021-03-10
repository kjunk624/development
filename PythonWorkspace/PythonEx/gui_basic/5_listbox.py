from tkinter import *

root = Tk()
root.title("Python_GUI")
root.geometry("640x480")

listbox = Listbox(root, selectmode="extended", height=0)#모든 목록이 보임
listbox.insert(0,"사과")
listbox.insert(1,"딸기")
listbox.insert(2,"바나나")
listbox.insert(3,"수박")
listbox.insert(4,"포도")
listbox.pack()

def btncmd():
    # 삭제
    #listbox.delete(0) # 맨 앞 항목을 삭제

    # 갯수 확인
    #print("리스트에는", listbox.size(),"개가 있어요")

    # 항목 확인(시작idx, 끝idx)
    #print("1번째 부터 3번째 까지의 항목 : ", listbox.get(0,2))

    # 선택된 항목 확인(위치로 반환 ex) (1,2,3))
    print("선택된 항목 : ", listbox.curselection())


    

btn = Button(root,text="클릭", command=btncmd)
btn.pack()

root.mainloop()