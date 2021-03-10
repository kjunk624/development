from random import *
from tkinter import *

# def random_colour_code():
#     hex_chars = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
#     colour_code = "#"
#     for i in range(0, 6):
#         colour_code = colour_code + choice(hex_chars)
#     return colour_code

# def random_colour_code():
#     # colour_code = f"#{randint(0, 0xffffff):06x}"
#     # return colour_code
#     return f"#{randint(0, 0xffffff):06x}"


my_window = Tk()
my_canvas = Canvas(my_window, width=300, height=300, bg="white")
my_canvas.grid(row=0, column=0)

for i in range(0, 400): # 무한 반복 되는 문제해결
    x1 = randint(0, 300)
    y1 = randint(0, 300)
    x2 = randint(0, 300)
    y2 = randint(0, 300)
    random_width = randint(1, 25)
    # my_canvas.create_line(x1, y1, x2, y2, fill=random_colour_code(), width=random_width)
    my_canvas.create_line(x1, y1, x2, y2,
                          fill=f"#{randint(0, 0xffffff):06x}", # 코드는 간단 하지만 추후 혼동을 유발 할 수 있다.
                          width=random_width)                  # '06x' -> 자리수? ex) #a2f931
    my_canvas.update()

    var1 = 255
    print(var1, type(var1))
    var2 = f"{var1}"
    print(var2, type(var2))
    var3 = f"{var1: 0x}"
    print(var3, type(var3))
    print()
    print(f"{var1:0x}") # ff
    print(f"{var1:01x}") # ff
    print(f"{var1:02x}") # ff
    print(f"{var1:03x}") # 0ff
    print(f"{var1:04x}") # 00ff
    print(f"{var1:05x}") # 000ff
    print(f"{var1:06x}") # 0000ff


my_window.mainloop()

