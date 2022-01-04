from .polygon import Polygon
from pyth3d.math import Vector3


class Object:
    def __init__(self, *args: Polygon):
        self.faces = (
            face for face in args
        )

    def add_face(self, face):
        self.faces += (face,)

    def draw(self, view: Vector3, drawer):
        for polygon in self.faces:
            if (view - polygon.direction()).length() < (view + polygon.direction()).length() or True:
                polygon.draw(view, drawer)
