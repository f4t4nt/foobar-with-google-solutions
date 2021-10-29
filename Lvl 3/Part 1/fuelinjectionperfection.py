def mult2(x):
    rv, carry_over, x = "", False, x[::-1]
    for i in x:
        new_char = int(i) * 2
        if carry_over:
            new_char += 1
            carry_over = False
        if new_char > 9:
            new_char %= 10
            carry_over = True
        rv += str(new_char)
    if carry_over:
        rv += '1'
    rv = rv[::-1]
    return rv

def div2(x):
    rv, x = "", x[::-1]
    for i in x:
        if int(i) % 2 == 1:
            tmp = rv[-1]
            rv = rv[:-1]
            rv += str(int(tmp) + 5)
        new_char =  int(int(i) / 2)
        rv += str(new_char)
    if rv[-1] == '0':
        rv = rv[:-1]
    rv = rv[::-1]
    return rv

def comp(a, b): # a >= b
    if a == b:
        return True
    elif len(a) > len(b):
        return True
    elif len(b) > len(a):
        return False
    elif a[0] == b[0]:
        return comp(a[1:], b[1:])
    elif a[0] > b[0]:
        return True
    else:
        return False

def sub(a, b):
    rv, carry_over, a, b = "", False, a[::-1], b[::-1]
    for i in range(len(b)):
        new_char = int(a[i]) - int(b[i])
        if carry_over:
            new_char -= 1
            carry_over = False
        if new_char < 0:
            new_char %= 10
            carry_over = True
        rv += str(new_char)
    for i in range(len(b), len(a)):
        new_char = int(a[i])
        if carry_over:
            new_char -= 1
            carry_over = False
        if new_char < 0:
            new_char %= 10
            carry_over = True
        rv += str(new_char)
    while rv[-1] == '0':
        rv = rv[:-1]
    rv = rv[::-1]
    return rv

def add(a, b):
    rv, carry_over, a, b = "", False, a[::-1] + "0", b[::-1]
    for i in range(len(b)):
        new_char = int(a[i]) + int(b[i])
        if carry_over:
            new_char += 1
            carry_over = False
        if new_char > 9:
            new_char %= 10
            carry_over = True
        rv += str(new_char)
    for i in range(len(b), len(a)):
        new_char = int(a[i])
        if carry_over:
            new_char += 1
            carry_over = False
        if new_char > 9:
            new_char %= 10
            carry_over = True
        rv += str(new_char)
    while rv[-1] == '0':
        rv = rv[:-1]
    rv = rv[::-1]
    return rv

def reduce(n, x):
    while len(n) > 0 and int(n[-1]) % 2 == 0:
        n = div2(n)
        x += 1
    return n, x

def solution(n):
    n, x = reduce(n, 0)
    bfs, rv = [[n, x]], {}
    while len(bfs) > 0:
        a, b = bfs[0][0], bfs[0][1]
        if len(a) > 0 and (not a in rv or rv[a] > b):
            rv[a] = b
            ap1, b1 = reduce(add(a, '1'), b + 1)
            am2, b2 = reduce(sub(a, '1'), b + 1)
            bfs += [[ap1, b1], [am2, b2]]
        bfs = bfs[1:]
    return rv['1']

# CHECK WHETHER TERMS MATCH UP
# 
# rv, q, i = [1000] * 10000, [[1,0]], 0
# 
# while i < len(rv) * len(rv) and len(q) > 0:
#     a, b = q[0][0], q[0][1]
#     if 0 < a and a < len(rv) and rv[a] > b:
#         rv[a] = b
#         b += 1
#         q += [[a + 1, b], [a - 1, b], [2 * a, b]]
#     q = q[1:]
#     i += 1
# 
# for x in range(1, len(rv)):
#     assert(rv[x] == solution(str(x)))