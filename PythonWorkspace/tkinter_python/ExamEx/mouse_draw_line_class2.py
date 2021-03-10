from tkinter import*

class DrawLineApp():
    def __init__(self, the_window, width, height, colour, row, column):
        self.my_canvas = Canvas(the_window, width=width, height=height, bg=colour)
        self.my_canvas.grid(row=row, column=column)
        self.my_canvas.bind("<Button-1>", self.draw_line)
        self.click_number=0
        self.x1=0
        self.y1=0
        self.x2=0
        self.y2=0

    def draw_line(self, event):
        if self.click_number == 0:
            self.x1 = event.x
            self.y1 = event.y
            self.click_number = 1
        else:
            self.x2 = event.x
            self.y2 = event.y
            self.my_canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill="black", width=10)
            self.click_number = 0


my_window = Tk()
my_draw_line1 = DrawLineApp(my_window, width=400, height=400, colour="white", row=0, column=0)
my_draw_line2 = DrawLineApp(my_window, width=400, height=400, colour="yellow", row=0, column=1)

my_window.mainloop()