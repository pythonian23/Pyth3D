from .vector import Vector


class Vector2 (Vector):
    _dimensions = 2

    def __init__(self, *args):
        super().__init__(*args)
        self.x = property(self.get_x, self.set_x)
        self.y = property(self.get_y, self.set_y)

    def get_x(self):
        return self._vector[0]

    def set_x(self, x):
        self._vector[0] = x

    def get_y(self):
        return self._vector[1]

    def set_y(self, y):
        self._vector[1] = y
