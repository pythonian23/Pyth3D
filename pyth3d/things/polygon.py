from ..math import Vector3


class Polygon:
    def __init__(self,
                 shape=(Vector3(), Vector3(), Vector3()),
                 name="Unnamed"):
        self.shape = [
            Vector3(coord) for coord in shape
        ]
        self.name = name

    def direction(self):
        return (self.shape[0]-self.shape[1]).perpendicular(self.shape[0]-self.shape[2])
