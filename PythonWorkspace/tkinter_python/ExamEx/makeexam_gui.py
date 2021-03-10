from tkinter import *
import requests
from bs4 import BeautifulSoup

win = Tk()
win.geometry("640x480")

ent = Entry(win)
# ent.insert(0, "0")
ent.pack()


# def ent_p():
#     a = ent.get()
#     print(a)


def lotto_p() -> object:
    n = ent.get()
    url = "https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={}".format(n)
    # div class = "win_result"

    req = requests.get(url)
    # req.text
    soup = BeautifulSoup(req.text, "html.parser")
    txt = soup.find("div", attrs={"class", "win_result"}).get_text()

    # num_list = txt.split("\n")
    num_list = txt.split("\n")[7:13]

    # bonus = txt.split("\n")
    bonus = txt.split("\n")[-4]

    lab2 = Label(win, text=num_list)
    lab2.pack()
    lab3 = Label(win, text=bonus)
    lab3.pack()
    # print("당첨번호")
    # # print(txt)
    # print(num_list)
    # print("보너스 번호")
    # print(bonus)
    # # print(soup)


lot = lotto_p()

lab1 = Label(win)
lab1.config(textvariable=lot)
lab1.config(width=10, height=3)
lab1.pack()

# text = Text(win)
# text.config(width=30, height=5)
# text.pack()
# text.insert("1.0", str(lot))

btn = Button(win)
btn.config(text="로또 당첨 번호 확인")
btn.config(command=lotto_p)
btn.pack()

win.mainloop()
