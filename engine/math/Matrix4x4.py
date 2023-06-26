import math
from sys import float_info
from typing import Optional, Union

import numpy as np
from Vec3D import Vec3D
from Vec4D import Vec4D


class Matrix4x4:
    def __init__(
        self, values: Union[list[list[float]], np.ndarray, None] = None
    ) -> None:
        if values is None:
            self._arr = np.zeros((4, 4), dtype=np.float32)
        elif isinstance(values, np.ndarray) and values.shape == (4, 4):
            self._arr = values.astype(np.float32)
        elif (
            isinstance(values, list)
            and len(values) == 4
            and all(len(row) == 4 for row in values)
        ):
            self._arr = np.array(values, dtype=np.float32)
        else:
            raise ValueError("Invalid input values for Matrix4x4")

    def __str__(self) -> str:
        return str(self._arr)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._arr.tolist()})"

    def __copy__(self) -> "Matrix4x4":
        return Matrix4x4(self._arr)

    def __mul__(
        self, other: Union["Matrix4x4", Vec4D, Vec3D]
    ) -> Union["Matrix4x4", Vec4D, Vec3D]:
        if isinstance(other, Matrix4x4):
            return Matrix4x4(self._arr.dot(other._arr))
        elif isinstance(other, Vec4D):
            temp = np.array([other.x, other.y, other.z, other.w])
            temp = self._arr.dot(temp)
            return Vec4D(temp[0], temp[1], temp[2], temp[3])
        elif isinstance(other, Vec3D):
            return Vec3D(
                self._arr[0][0] * other.x
                + self._arr[0][1] * other.y
                + self._arr[0][2] * other.z,
                self._arr[1][0] * other.x
                + self._arr[1][1] * other.y
                + self._arr[1][2] * other.z,
                self._arr[2][0] * other.x
                + self._arr[2][1] * other.y
                + self._arr[2][2] * other.z,
            )
        else:
            raise NotImplementedError("Can only multiply Matrix4x4 by a Matrix4x4")

    def Identity(self) -> "Matrix4x4":
        temp = np.zeros((4, 4), dtype=np.float32)
        temp[0][0] = 1.0
        temp[1][1] = 1.0
        temp[2][2] = 1.0
        temp[3][4] = 1.0
        return temp

    def Constant(value: Union[int, float]):
        pass
