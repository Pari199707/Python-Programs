def kangaroo(x1, v1, x2, v2):
    if v1 == v2:
        return "NO"
    jumps = (x2-x1)/(v1-v2)
    if jumps > 0 and jumps.is_integer():
        return "YES"
    return "NO"
