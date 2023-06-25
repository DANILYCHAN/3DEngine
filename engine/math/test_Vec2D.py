import copy

from Vec2D import Vec2D, isNear

a = Vec2D(1.0, 2.0)
b = Vec2D(3, 4)

# testing copy
c = copy.copy(a)
assert isNear(c.x, 1) and isNear(c.y, 2)

# testing operator =
c = b
assert isNear(c.x, 3) and isNear(c.y, 4)

# testing .x & .y methods:
assert isNear(a.x, 1) and isNear(a.y, 2)
assert isNear(b.x, 3) and isNear(b.y, 4)

# testing operator -Vec:
neg = -a
assert isNear(neg.x, -a.x) and isNear(neg.y, -a.y)

# testing == & != operators:
assert c != a and c == b

# testing operators +, -:
summ = a + b
assert isNear(summ.x, 4) and isNear(summ.y, 6)
diff = a - b
assert isNear(diff.x, -2) and isNear(diff.y, -2)

# testing scaling operators:
scale1 = a * 2
assert isNear(scale1.x, 2) and isNear(scale1.y, 4)
scale2 = a / 2
assert isNear(scale2.x, 0.5) and isNear(scale2.y, 1)

# testing dot product:
dot = a.dot(b)
assert isNear(dot, 11)

dot = a @ b
assert isNear(dot, 11)

# testing .abs() & .normalized() methods:
assert isNear(abs(b), 5)
assert isNear(abs(b.normalized()), 1)
