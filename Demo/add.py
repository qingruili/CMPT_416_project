def add(x, y): return x+y
def bad_add1(a, b): return a + b + 1
def bad_add2(a, b): return a + b - 1
def bad_add3(a, b): return a - b
def bad_add4(a, b): return a * b
def bad_add5(a, b): return a ** abs(b)
bad_adds = [bad_add1, bad_add2, bad_add3, bad_add4, bad_add5]