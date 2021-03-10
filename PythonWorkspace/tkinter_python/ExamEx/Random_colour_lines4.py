from random import *
from tkinter import *

def random_colour_code():
    hex_chars = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
    colour_code = "#"
    for i in range(0, 6):
        colour_code = colour_code + choice(hex_chars)
    return colour_code


my_window = Tk()
my_canvas = Canvas(my_window, width=300, height=300, bg="white")
my_canvas.grid(row=0, column=0)

for i in range(0, 400): # 무한 반복 되는 문제해결
    x1 = randint(0, 300)
    y1 = randint(0, 300)
    x2 = randint(0, 300)
    y2 = randint(0, 300)
    random_width = randint(1, 25)
    my_canvas.create_line(x1, y1, x2, y2, fill=random_colour_code(), width=random_width)
    my_canvas.update()

my_window.mainloop()