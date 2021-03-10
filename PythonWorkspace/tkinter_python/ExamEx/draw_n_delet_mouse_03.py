from tkinter import *
from random import *

def random_line(event):
    x1 = randint(0,400)
    y1 = randint(0,400)
    x2 = randint(0,400)
    y2 = randint(0,400)
    my_canvas.create_line(x1, y1, x2, y2, fill=f'#{randint(0, 0xfffff):06x}', width=20)

def delete_lines(event):
    my_canvas.delete('all')

def display_coordinates(event):
    my_label['text'] =f'x={event.x} y={event.y}'

my_window = Tk()
my_canvas = Canvas(my_window, width=400, height=400, bg='white')
my_label = Label(bd=4, relief="solid", font="Times 22 bold", bg="white", fg="black")

# draw with mouse
my_canvas.bind('<Button-1>', display_coordinates)
my_canvas.grid(row=0, column=0)
my_label.grid(row=1, column=0)

my_window.mainloop()