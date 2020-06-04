"""
File: pyramid.py
----------------
YOUR DESCRIPTION HERE
"""


import tkinter
import time
import random
from PIL import ImageTk
from PIL import Image

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 600

COLUMNS = 8
ROWS = 8
SIZE = 100

def main():
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'Awesome')
    # a line for good measure!
    canvas.create_line(0, 0, 600, 600)

    # a blue square with width and height = 80
    canvas.create_rectangle(70, 70, 150, 150, fill="blue")
    # a yellow rectangle that is long and skinny
    canvas.create_rectangle(620, 100, 640, 510, fill="yellow")

    # a red oval and a rectangle at the exact same spot!
    canvas.create_rectangle(250, 150, 500, 500)
    canvas.create_oval     (250, 150, 500, 500, fill="red", outline="red")

    # images require the pillow library
    image = ImageTk.PhotoImage(Image.open("images/tutu.jpeg"))
    canvas.create_image(0,300,anchor="nw",image=image)

    # some text is written on the screen.
    canvas.create_text(20, 200, anchor='w', font='Courier 52', text='Programming is Awesome!')

    # dude, where's my rect?
    canvas.create_rectangle(0, 800, 10, 810)

    canvas_two = make_canvas(1000, 1000, 'My First Canvas')

    canvas_two.create_text(100, 700, anchor='w', font='Courier 33', text='First Canvass!!!!!!')

    for row in range(COLUMNS):
        for col in range(ROWS):
            create_chess = rectangles(canvas_two, row, col)
    canvas_two.mainloop()

    canvas_three = make_canvas(600, 600, 'Move Square')
    start_y = (CANVAS_HEIGHT / 2) - (SIZE / 2)
    end_y = start_y + SIZE
    rect = canvas_three.create_rectangle(10, start_y, SIZE, end_y, fill='black')

    while True:
        canvas_three.move(rect, 1, 1)
        canvas_three.update()

        time.sleep(1/50)

    canvas_three.mainloop()

def stop_sign():
    while
def rectangles(canvastwo, row, col):
    x = col * SIZE
    y = row * SIZE
    color = coloring(row, col)
    canvastwo = canvastwo.create_rectangle(x, y, x + SIZE, y + SIZE, fill=color)

def coloring(row, col):
    if (row + col) % 2 == 0:
        return 'black'





def mouse_moved(event):
    print('x = ' + str(event.x), 'y = ' + str(event.y))

######## DO NOT MODIFY ANY CODE BELOW THIS LINE ###########

# This function is provided to you and should not be modified.
# It creates a window that contains a drawing canvas that you
# will use to make your drawings.
def make_canvas(width, height, title=None):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    objects = {}
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    if title:
        top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()

    canvas.bind("<Motion>", mouse_moved)
    return canvas




if __name__ == '__main__':
    main()
