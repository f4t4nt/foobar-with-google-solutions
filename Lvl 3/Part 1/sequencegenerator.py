rv, q, i = [1000] * 1000, [[1,0]], 0

while i < 1000000 and len(q) > 0:
    a, b = q[0][0], q[0][1]
    if 0 < a and a < len(rv) and rv[a] > b:
        rv[a] = b
        b += 1
        q += [[a + 1, b], [a - 1, b], [2 * a, b]]
    q = q[1:]
    i += 1

print(rv[1:])