import copy
import math

from Vec3D import Vec3D, isNear

a = Vec3D(1.0, 2.0, 3)
b = Vec3D(3, 4, 5)

# testing copy
c = copy.copy(a)
assert isNear(c.x, 1) and isNear(c.y, 2) and isNear(c.z, 3)

# testing operator =
c = b
assert isNear(c.x, 3) and isNear(c.y, 4) and isNear(c.z, 5)

# testing .x & .y & .z methods:
assert isNear(a.x, 1) and isNear(a.y, 2) and isNear(a.z, 3)
assert isNear(b.x, 3) and isNear(b.y, 4) and isNear(b.z, 5)

# testing operator -Vec:
neg = -a
assert isNear(neg.x, -a.x) and isNear(neg.y, -a.y) and isNear(neg.z, -a.z)

# testing == & != operators:
assert c != a and c == b

# testing operators +, -:
summ = a + b
assert isNear(summ.x, 4) and isNear(summ.y, 6) and isNear(summ.z, 8)
diff = a - b
assert isNear(diff.x, -2) and isNear(diff.y, -2) and isNear(diff.z, -2)

# testing scaling operators:
scale1 = a * 2
assert isNear(scale1.x, 2) and isNear(scale1.y, 4) and isNear(scale1.z, 6)
scale2 = a / 2
assert isNear(scale2.x, 0.5) and isNear(scale2.y, 1) and isNear(scale2.z, 1.5)

# testing dot product:
dot = a.dot(b)
assert isNear(dot, 26)

dot = a @ b
assert isNear(dot, 26)

# testing cross product
cross = a.cross(b)
cross_neg = b.cross(a)
assert isNear(a.dot(cross), 0) and isNear(b.dot(cross), 0)
assert cross == -cross_neg

# testing .abs() & .normalized() methods:
assert isNear(abs(b), math.sqrt(50))
assert isNear(abs(b.normalized()), 1)
