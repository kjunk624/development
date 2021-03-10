from tkinter import *
from random import *

def random_line():
    x1 = randint(0,400)
    y1 = randint(0,400)
    x2 = randint(0,400)
    y2 = randint(0,400)
    my_canvas.create_line(x1, y1, x2, y2, fill=f'#{randint(0, 0xfffff):06x}', width=20)

def delete_lines():
    my_canvas.delete('all')


my_window = Tk()
my_canvas = Canvas(my_window, width=400, height=400, bg='white')
mybtn1 = Button(my_window, text='Click for a random coloured line', command=random_line)
mybtn2 = Button(my_window, text='Click to clear coloured lines', command=delete_lines)
my_canvas.grid(row=0, column=0)
mybtn1.grid(row=1, column=0)
mybtn2.grid(row=2, column=0)

my_window.mainloop()