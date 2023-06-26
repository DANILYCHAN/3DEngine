import math
from sys import float_info
from typing import Union

from Vec4D import Vec4D


class Vec3D:
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0) -> None:
        self.x, self.y, self.z = x, y, z

    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"

    def __repr__(self) -> str:
        return repr((self.x, self.y, self.z))

    def __copy__(self) -> "Vec3D":
        return Vec3D(self.x, self.y, self.z)

    def fromVec4D(self, other: Vec4D) -> "Vec3D":
        if isinstance(other, Vec4D):
            return Vec3D(other.x, other.y, other.z)
        raise TypeError("Can only create Vec3D from Vec4D")

    def dot(self, other: "Vec3D") -> float:
        if not isinstance(other, Vec3D):
            raise TypeError("Can only take dot product of two Vector3D objects")
        return self.x * other.x + self.y * other.y + self.z * other.z

    __matmul__ = dot  # we can use both a @ b and a.dot(b)

    def __sub__(self, other: "Vec3D") -> "Vec3D":
        if not isinstance(other, Vec3D):
            raise TypeError("Can only subtract two Vector3D objects")
        return Vec3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __add__(self, other: "Vec3D") -> "Vec3D":
        if not isinstance(other, Vec3D):
            raise TypeError("Can only add two Vector3D objects")
        return Vec3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, scalar: Union[float, int]) -> "Vec3D":
        if isinstance(scalar, int) or isinstance(scalar, float):
            return Vec3D(self.x * scalar, self.y * scalar, self.z * scalar)
        raise NotImplementedError("Can only multiply Vec3D by a scalar")

    def __rmul__(self, scalar: float) -> "Vec3D":
        return self.__mul__(scalar)

    def __neg__(self) -> "Vec3D":
        return Vec3D(-self.x, -self.y, -self.z)

    def __truediv__(self, scalar: Union[float, int]) -> "Vec3D":
        if isinstance(scalar, float) or isinstance(scalar, int):
            return Vec3D(self.x / scalar, self.y / scalar, self.z / scalar)
        raise NotImplementedError("Can only divide Vec3D by a scalar")

    def sqrAbs(self) -> Union[int, float]:
        return self.x**2 + self.y**2 + self.z**2

    def __abs__(self):
        return math.sqrt(self.sqrAbs())

    def __eq__(self, other: "Vec3D") -> bool:
        if isinstance(other, Vec3D):
            diff = self - other
            return diff.sqrAbs() < float_info.epsilon
        return False

    def __ne__(self, other: "Vec3D") -> bool:
        return not (self == other)

    def normalized(self) -> "Vec3D":
        vecAbs = abs(self)
        if vecAbs > float_info.epsilon:
            return Vec3D(self.x, self.y, self.z) / vecAbs
        else:
            return Vec3D(0, 0, 0)

    def cross(self, other: "Vec3D") -> "Vec3D":
        if isinstance(other, Vec3D):
            return Vec3D(
                self.y * other.z - other.y * self.z,
                self.z * other.x - other.z * self.x,
                self.x * other.y - other.x * self.y,
            )

    def makePoint4D(self) -> Vec4D:
        return Vec4D(self.x, self.y, self.z, 1.0)


def isNear(x: float, y: float) -> bool:
    return abs(x - y) < float_info.epsilon
