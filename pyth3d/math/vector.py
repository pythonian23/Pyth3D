from .types import VectorThing, vector, scalar
import math


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

    def __bool__(self):
        return True

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

    def __lshift__(self, n):
        out = self.__copy__()
        for i in range(n):
            out._vector.append(out._vector.pop(0))
        return out

    def __rshift__(self, n):
        out = self.__copy__()
        for i in range(n):
            out._vector.insert(0, out._vector.pop())
        return out

    def __eq__(self, other):
        obj = self.__class__(other)
        return all((self._vector[i] == obj._vector[i] for i in range(self._dimensions)))

    def dot(self, other):
        return sum(self * other)

    inner = dot

    def norm(self):
        return sum(self**2)**(1/2)

    magnitude = length = norm

    def unit(self):
        return self/self.norm()

    direction = unit

    def cos(self, other):
        return self.unit().dot(self.__class__(other).unit())

    def sin(self, other):
        return (1-self.cos(other)**2)**(1/2)

    def angle(self, other):
        return math.acos(self.cos(other))

    def projected_length(self, other):
        return self.norm()*self.cos(other)

    def project(self, other):
        return self.projected_length(other)*other.unit
