import math
from sys import float_info
from typing import Union


class Vec4D:
    def __init__(
        self, x: float = 0.0, y: float = 0.0, z: float = 0.0, w: float = 0.0
    ) -> None:
        self.x, self.y, self.z, self.w = x, y, z, w

    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.z}, {self.w})"

    def __repr__(self) -> str:
        return repr((self.x, self.y, self.z, self.w))

    def __copy__(self):
        return Vec4D(self.x, self.y, self.z, self.w)

    def __sub__(self, other: "Vec4D") -> "Vec4D":
        if not isinstance(other, Vec4D):
            raise TypeError("Can only subtract two Vector4D objects")
        return Vec4D(
            self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w
        )

    def __add__(self, other: "Vec4D") -> "Vec4D":
        if not isinstance(other, Vec4D):
            raise TypeError("Can only add two Vector4D objects")
        return Vec4D(
            self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w
        )

    def __mul__(self, scalar: Union[float, int]) -> "Vec4D":
        if isinstance(scalar, int) or isinstance(scalar, float):
            return Vec4D(
                self.x * scalar, self.y * scalar, self.z * scalar, self.w * scalar
            )
        raise NotImplementedError("Can only multiply Vec4D by a scalar")

    def __rmul__(self, scalar: float) -> "Vec4D":
        return self.__mul__(scalar)

    def __neg__(self) -> "Vec4D":
        return Vec4D(-self.x, -self.y, -self.z, -self.w)

    def __truediv__(self, scalar: Union[float, int]) -> "Vec4D":
        if isinstance(scalar, float) or isinstance(scalar, int):
            return Vec4D(
                self.x / scalar, self.y / scalar, self.z / scalar, self.w / scalar
            )
        raise NotImplementedError("Can only divide Vec4D by a scalar")

    def sqrAbs(self) -> Union[int, float]:
        return self.x**2 + self.y**2 + self.z**2 + self.w**2

    def __abs__(self):
        return math.sqrt(self.sqrAbs())

    def __eq__(self, other: "Vec4D") -> bool:
        if isinstance(other, Vec4D):
            diff = self - other
            return diff.sqrAbs() < float_info.epsilon
        return False

    def __ne__(self, other: "Vec4D") -> bool:
        return not (self == other)

    def normalized(self) -> "Vec4D":
        vecAbs = abs(self)
        if vecAbs > float_info.epsilon:
            return Vec4D(self.x, self.y, self.z, self.w) / vecAbs
        else:
            return Vec4D(0, 0, 0, 0)


def isNear(x: float, y: float) -> bool:
    return abs(x - y) < float_info.epsilon
