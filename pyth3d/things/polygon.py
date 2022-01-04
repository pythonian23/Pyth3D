from pyth3d.math import Vector3
from pyth3d.graphics import Drawer


class Polygon:
    def __init__(self,
                 shape=(Vector3(), Vector3(), Vector3()),
                 position=Vector3(),
                 name="Unnamed"):
        self.shape = (
            Vector3(coord) for coord in shape
        )
        self.position = Vector3(position)
        self.name = name

    def direction(self):
        # TODO: Learn vectors and stuff
        return 0

    def draw(self, view: Vector3, drawer: Drawer):
        print(self.name, "Drawn")
        drawer.polygon(self.shape)
