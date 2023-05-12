def all_diff(a, b, c): return a != b and b != c and a != c
def bad_all_diff1(a, b, c): return a != b and b != c
def bad_all_diff2(a, b, c): return a != b or b != c or a != c
def bad_all_diff3(a, b, c): return a == b and b == c and a == c
def bad_all_diff4(a, b, c): return not (a == b and b == c and a == c)
bad_all_diffs = [bad_all_diff1, bad_all_diff2, bad_all_diff3, bad_all_diff4]