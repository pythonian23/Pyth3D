from .types import VectorThing, vector, scalar


class Vector (VectorThing):
    _dimensions = 0

    def __init__(self, *args):
        if len(args) == 0:
            self._vector = [0]*self._dimensions
        elif len(args) == 1:
            if isinstance(args[0], vector):
                self._vector = [args[0][i] for i in range(self._dimensions)]
            elif isinstance(args[0], scalar):
                self._vector = [args[0]] * self._dimensions
        elif len(args) == self._dimensions:
            self._vector = [args[i] for i in range(self._dimensions)]
        else:
            raise TypeError(f"Type {type(args[0])} not supported.")

    def __len__(self):
        return self._dimensions

    def __str__(self):
        return str(tuple(self._vector))

    def __repr__(self):
        return f"{self.__class__.__name__}{tuple(self._vector)}"

    def __iter__(self):
        return iter(self._vector)

    def __copy__(self):
        return self.__class__(self._vector.copy())

    def __add__(self, other):
        out = self.__class__()
        obj = self.__class__(other)
        for i in range(self._dimensions):
            out._vector[i] = self._vector[i] + obj._vector[i]
        return out

    def __sub__(self, other):
        out = self.__class__()
        obj = self.__class__(other)
        for i in range(self._dimensions):
            out._vector[i] = self._vector[i] - obj._vector[i]
        return out

    def __mul__(self, other):
        out = self.__class__()
        obj = self.__class__(other)
        for i in range(self._dimensions):
            out._vector[i] = self._vector[i] * obj._vector[i]
        return out

    def __truediv__(self, other):
        out = self.__class__()
        obj = self.__class__(other)
        for i in range(self._dimensions):
            out._vector[i] = self._vector[i] / obj._vector[i]
        return out

    def __pow__(self, power, modulo=None):
        if modulo is None:
            modulo = float("inf")
        out = self.__class__()
        obj = self.__class__(power)
        for i in range(self._dimensions):
            out._vector[i] = (self._vector[i] ** obj._vector[i]) % modulo
        return out

    def __getitem__(self, item):
        return self._vector.__getitem__(item)

    def __setitem__(self, key, value):
        self._vector.__setitem__(key, value)

    def dot(self, other):
        return sum(self * other)

    inner = dot

    def norm(self):
        return sum(self**2)**(1/2)

    magnitude = length = norm

    # TODO: Projection
    # TODO: Angle
