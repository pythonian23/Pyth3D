import turtle
from .drawer import Drawer


class TurtleDrawer (Drawer):
    def __lib_init__(self, *args, window=None, pen=None, screensize=None, bg="black"):
        if window is None:
            self.window = turtle.Screen()
        else:
            self.window = window
        self.window.tracer(0)

        setup = {}
        if screensize:
            setup["canvwidth"] = screensize[0]
            setup["canvheight"] = screensize[1]
        self.window.screensize(bg=bg, **setup)

        if pen is None:
            self.pen = turtle.Turtle()
            self.pen.hideturtle()
            self.pen.penup()
            self.pen.speed(0)
        else:
            self.pen = pen

    def __draw__(self, coord0, coord1, coord2, *args, color=(1, 0, 1)):
        self.pen.goto(coord0)
        self.pen.color(color)
        self.pen.begin_fill()
        self.pen.goto(coord1)
        self.pen.goto(coord2)
        self.pen.goto(coord0)
        self.pen.end_fill()

    def __update__(self, *args, **kwargs):
        self.window.update()
        self.pen.clear()
