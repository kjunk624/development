from tkinter import *

root = Tk()
ent = Entry(root)
ent.pack()


def click():
    ent_text = ent.get()
    lab = Label(root, text=ent_text)
    lab.pack()


btn = Button(root, text="Click Me!", command=click)
btn.pack()

root.mainloop()
