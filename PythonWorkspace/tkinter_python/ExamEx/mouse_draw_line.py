from tkinter import*

def draw_line(event):
    global click_number
    global x1, y1
    if click_number == 0:
        x1 = event.x
        y1 = event.y
        click_number = 1
    else:
        x2 = event.x
        y2 = event.y
        my_canvas.create_line(x1, y1, x2, y2, fill="black", width=10)
        click_number = 0


my_window = Tk()
my_canvas = Canvas(my_window, width=400, height=400)
my_canvas.grid(row=0, column=0)
my_canvas.bind("<Button-1>", draw_line)
click_number = 0
my_window.mainloop()