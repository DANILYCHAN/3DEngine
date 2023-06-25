import copy
import math

from Vec4D import Vec4D, isNear

a = Vec4D(1, 2, 3, 4)
b = Vec4D(3, 4, 5, 6)

# testing copy
c = copy.copy(a)
assert isNear(c.x, 1) and isNear(c.y, 2) and isNear(c.z, 3) and isNear(c.w, 4)

# testing operator =
c = b
assert isNear(c.x, 3) and isNear(c.y, 4) and isNear(c.z, 5) and isNear(c.w, 6)

# testing .x & .y & .z & .wmethods:
assert isNear(a.x, 1) and isNear(a.y, 2) and isNear(a.z, 3) and isNear(a.w, 4)
assert isNear(b.x, 3) and isNear(b.y, 4) and isNear(b.z, 5) and isNear(b.w, 6)

# testing operator -Vec:
neg = -a
assert (
    isNear(neg.x, -a.x)
    and isNear(neg.y, -a.y)
    and isNear(neg.z, -a.z)
    and isNear(neg.w, -a.w)
)

# testing == & != operators:
assert c != a and c == b

# testing operators +, -:
summ = a + b
assert (
    isNear(summ.x, 4) and isNear(summ.y, 6) and isNear(summ.z, 8) and isNear(summ.w, 10)
)
diff = a - b
assert (
    isNear(diff.x, -2)
    and isNear(diff.y, -2)
    and isNear(diff.z, -2)
    and isNear(diff.w, -2)
)

# testing scaling operators:
scale1 = a * 2
assert (
    isNear(scale1.x, 2)
    and isNear(scale1.y, 4)
    and isNear(scale1.z, 6)
    and isNear(scale1.w, 8)
)
scale2 = a / 2
assert (
    isNear(scale2.x, 0.5)
    and isNear(scale2.y, 1)
    and isNear(scale2.z, 1.5)
    and isNear(scale2.w, 2)
)

# testing .abs() & .normalized() methods:
assert isNear(abs(b), math.sqrt(86))
assert isNear(abs(b.normalized()), 1)
