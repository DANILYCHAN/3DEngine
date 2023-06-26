import math
from sys import float_info
from typing import Union

from Vec4D import Vec4D


class Vec2D:
    def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
        self.x, self.y = x, y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return repr((self.x, self.y))

    def __copy__(self) -> "Vec2D":
        return Vec2D(self.x, self.y)

    def fromVec4D(self, other: Vec4D) -> "Vec2D":
        if isinstance(other, Vec4D):
            return Vec2D(other.x, other.y)
        raise TypeError("Can only create Vec2D from Vec4D")

    def dot(self, other: "Vec2D") -> float:
        if not isinstance(other, Vec2D):
            raise TypeError("Can only take dot product of two Vector2D objects")
        return self.x * other.x + self.y * other.y

    __matmul__ = dot  # we can use both a @ b and a.dot(b)

    def __sub__(self, other: "Vec2D") -> "Vec2D":
        if not isinstance(other, Vec2D):
            raise TypeError("Can only subtract two Vector2D objects")
        return Vec2D(self.x - other.x, self.y - other.y)

    def __add__(self, other: "Vec2D") -> "Vec2D":
        if not isinstance(other, Vec2D):
            raise TypeError("Can only add two Vector2D objects")
        return Vec2D(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar: Union[float, int]) -> "Vec2D":
        if isinstance(scalar, int) or isinstance(scalar, float):
            return Vec2D(self.x * scalar, self.y * scalar)
        raise NotImplementedError("Can only multiply Vec2D by a scalar")

    def __rmul__(self, scalar: float) -> "Vec2D":
        return self.__mul__(scalar)

    def __neg__(self) -> "Vec2D":
        return Vec2D(-self.x, -self.y)

    def __truediv__(self, scalar: Union[float, int]) -> "Vec2D":
        if isinstance(scalar, float) or isinstance(scalar, int):
            return Vec2D(self.x / scalar, self.y / scalar)
        raise NotImplementedError("Can only divide Vec2D by a scalar")

    def sqrAbs(self) -> Union[int, float]:
        return self.x**2 + self.y**2

    def __abs__(self):
        return math.sqrt(self.sqrAbs())

    def __eq__(self, other: "Vec2D") -> bool:
        if isinstance(other, Vec2D):
            diff = self - other
            return diff.sqrAbs() < float_info.epsilon
        return False

    def __ne__(self, other: "Vec2D") -> bool:
        return not (self == other)

    def normalized(self) -> "Vec2D":
        vecAbs = abs(self)
        if vecAbs > float_info.epsilon:
            return Vec2D(self.x, self.y) / vecAbs
        else:
            return Vec2D(0, 0)

    def makePoint4D(self) -> Vec4D:
        return Vec4D(self.x, self.y, 1.0, 1.0)


def isNear(x: float, y: float) -> bool:
    return abs(x - y) < float_info.epsilon
