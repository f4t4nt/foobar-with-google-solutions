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
    while len(rv) > 0 and rv[-1] == '0':
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
    while len(rv) > 0 and rv[-1] == '0':
        rv = rv[:-1]
    rv = rv[::-1]
    return rv

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
    while len(rv) > 0 and rv[-1] == '0':
        rv = rv[:-1]
    rv = rv[::-1]
    return rv

def reduce(x, y):
    rv, pow2 = 0, [y]
    while comp(x, pow2[-1]):
        pow2 += [mult2(pow2[-1])]
    i = len(pow2) - 1
    while i > -1 and comp(x, '2') and comp(x, y):
        while comp(x, '2') and comp(x, pow2[i]):
            x = sub(x, pow2[i])
            rv += 2 ** i
        i -= 1
    return x, y, rv

def solution(x, y):
    valid, rv = False, 0
    while len(x) > 0 and len(y) > 0:
        if (x == '1' and y == '') or (y == '1' and x == '') or (x == '1' and y == '1'):
            break
        if comp(x, y):
            x, y, tmp = reduce(x, y)
        else:
            y, x, tmp = reduce(y, x)
        rv += tmp
    if x == '1' and y == '1':
        return str(rv)
    elif (x == '1' and y == '') or (y == '1' and x == ''):
        return str(rv - 1)
    else:
        return 'impossible'