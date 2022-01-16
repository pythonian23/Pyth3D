import math

from ..graphics.drawer import Drawer
from ..math.vector2 import Vector2
from ..math.vector3 import Vector3
from ..things.polygon import Polygon


class View:
    def __init__(
            self,
            position=(0, 0, 0),
            direction=(0, 0, 1),
            up=(0, 1, 0),
            size=(300, 300),
            pixels_per_radian=None
    ):
        self.set_position(position)
        self.set_direction(direction, up)
        if pixels_per_radian is None:
            self.ppr = 2*size[0]/math.pi
        else:
            self.ppr = pixels_per_radian
        self.angle_range = (size[0]/self.ppr, size[1]/self.ppr)
        self.plota = [0]
        self.plotb = [0]

    def set_position(self, position):
        self.position = Vector3(position)

    def set_direction(self, direction, up):  # TODO: Make up auto-set to a y-axis oriented direction, while also taking the direction into mind
        self.direction = Vector3(direction).unit()
        self.up = Vector3(up).unit()
        self.right = self.direction.cross(self.up)

    def draw_poly(self, poly: Polygon, drawer: Drawer):
        planar = [self.get_2d_projection(p) for p in poly.shape]
        inside = [self.in_screen(p) for p in planar]
        if planar[0][0] != self.plota[-1] and self.plota[-1]:
            print(self.direction)
            print(math.degrees(self.plotb[-1]))
        self.plota.append(planar[0][0])
        self.plotb.append(math.atan(self.direction[2]/self.direction[1]))
        if any(inside):  # TODO: Find out if the polygon's points outside the screen but intersects it
            drawer.polygon(*[tuple(p*self.ppr) for p in planar])

    def get_2d_projection(self, point: Vector3):
        try:
            x = math.atan((point.projected_length(self.right)/(self.position-point).norm()))
        except ZeroDivisionError:
            print("zdx")
            x = math.pi/2
        try:
            y = math.atan((point.projected_length(self.up)/(self.position-point).norm()))
        except ZeroDivisionError:
            print("zdy")
            y = math.pi/2

        return Vector2(x, y)

    def in_screen(self, point: Vector2):
        return (abs(point[0]) <= self.angle_range[0]) and (abs(point[1]) <= self.angle_range[1])
