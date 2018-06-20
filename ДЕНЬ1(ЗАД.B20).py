import datetime
def printTimeStamp(name):
    print('prodaivoda yan prodaivoda dan:' + name)
    print('Час компиляции:' + str(datetime.datetime.now()))
    
import tkinter as tk
from tkinter import Image

enum = 0
xxx = 0

BRD_ROWS = BRD_COLS = 8
CELL_SZ = 100

root = tk.Tk()

canvas = tk.Canvas(root, width=CELL_SZ * BRD_ROWS, height=CELL_SZ * BRD_COLS)

cell_colors = ['white', 'black']
ci = 0  # color index

for row in range(BRD_ROWS):
    for col in range(BRD_COLS):
        x1, y1 = col * CELL_SZ, row * CELL_SZ
        x2, y2 = col * CELL_SZ + CELL_SZ, row * CELL_SZ + CELL_SZ
        canvas.create_rectangle((x1, y1), (x2, y2), fill=cell_colors[ci])

        ci = not ci

    ci = not ci

photo = tk.PhotoImage(file="kong2.gif")
image = canvas.create_image(350, 450, image = photo)

def paint_oval():
    xy = canvas.coords(image)
    canvas.create_text(xy,fill="red", font=("Purisa", 30),
                       text=enum)

def calc(event):
    if enum == 0:
        paint(250, 650)
    elif enum == 1:
        paint(50, 750)
    elif enum == 2:
        paint(150, 550)
    elif enum == 3:
        paint(250, 750)
    elif enum == 4:
        paint(50, 650)
    elif enum == 5:
        paint(150, 450)
    elif enum == 6:
        paint(350, 550)
    elif enum == 7:
        paint(250, 350)
    elif enum == 8:
        paint(50, 250)
    elif enum == 9:
        paint(150, 50)
    elif enum == 10:
        paint(350, 150)
    elif enum == 11:
        paint(550, 250)
    elif enum == 12:
        paint(450, 50)
    elif enum == 13:
        paint(650, 150)
    elif enum == 14:
        paint(750, 350)
    elif enum == 15:
        paint(650, 550)
    elif enum == 16:
        paint(750, 750)
    elif enum == 17:
        paint(550, 650)
    elif enum == 18:
        paint(450, 450)
    elif enum == 19:
        paint(350, 250)
    elif enum == 20:
        paint(150, 350)
    elif enum == 21:
        paint(50, 150)
    elif enum == 22:
        paint(250, 50)
    elif enum == 23:
        paint(450, 150)
    elif enum == 24:
        paint(650, 50)
    elif enum == 25:
        paint(750, 250)
    elif enum == 26:
        paint(550, 350)
    elif enum == 27:
        paint(750, 450)
    elif enum == 28:
        paint(650, 650)
    elif enum == 29:
        paint(450, 750)
    elif enum == 30:
        paint(550, 550)
    elif enum == 31:
        paint(450, 350)
    elif enum == 32:
        paint(550, 150)
    elif enum == 33:
        paint(750, 50)
    elif enum == 34:
        paint(650, 250)
    elif enum == 35:
        paint(550, 50)
    elif enum == 36:
        paint(750, 150)
    elif enum == 37:
        paint(650, 350)
    elif enum == 38:
        paint(450, 250)
    elif enum == 39:
        paint(550, 450)
    elif enum == 40:
        paint(750, 550)
    elif enum == 41:
        paint(650, 750)
    elif enum == 42:
        paint(450, 650)
    elif enum == 43:
        paint(250, 550)
    elif enum == 44:
        paint(350, 750)
    elif enum == 45:
        paint(150, 650)
    elif enum == 46:
        paint(50, 450)
    elif enum == 47:
        paint(150, 250)
    elif enum == 48:
        paint(50, 50)
    elif enum == 49:
        paint(250, 150)
    elif enum == 50:
        paint(350, 350)
    elif enum == 51:
        paint(450, 550)
    elif enum == 52:
        paint(650, 450)
    elif enum == 53:
        paint(750, 650)
    elif enum == 54:
        paint(550, 750)
    elif enum == 55:
        paint(350, 650)
    elif enum == 56:
        paint(150, 750)
    elif enum == 57:
        paint(50, 550)
    elif enum == 58:
        paint(250, 450)
    elif enum == 59:
        paint(50, 350)
    elif enum == 60:
        paint(150, 150)
    elif enum == 61:
        paint(350, 50)
    elif enum == 62:
        paint(250, 250)


def paint(x, y):
    global enum
    enum += 1
    paint_oval()
    canvas.coords(image, x, y)
    print(canvas.coords(image))


root.bind('<Button-1>', calc)

canvas.pack()

root.mainloop()
