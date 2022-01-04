from .vector import Vector


class Vector3 (Vector):
    _dimensions = 3

    def __init__(self, *args):
        super().__init__(*args)
        self.x = property(self.get_x, self.set_x)
        self.y = property(self.get_y, self.set_y)
        self.z = property(self.get_z, self.set_z)

    def get_x(self):
        return self._vector[0]

    def set_x(self, x):
        self._vector[0] = x

    def get_y(self):
        return self._vector[1]

    def set_y(self, y):
        self._vector[1] = y

    def get_z(self):
        return self._vector[2]

    def set_z(self, z):
        self._vector[2] = z
