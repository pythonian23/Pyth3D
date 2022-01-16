from .polygon import Polygon
from .view import View
from ..graphics import Drawer


class Object:
    def __init__(self, *args: Polygon):
        self.faces = [
            face for face in args
        ]

    def add_face(self, face):
        self.faces += (face,)

    def draw(self, view: View, drawer: Drawer):
        for polygon in self.faces:
            view.draw_poly(polygon, drawer)
