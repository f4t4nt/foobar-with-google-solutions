import math

def simulate(i, j):
    i, j = max(i, j), min(i, j)
    past = { (i, j) }
    i -= j
    j += j
    while i != j and not (i, j) in past:
        i, j = max(i, j), min(i, j)
        past.add((i, j))
        i -= j
        j += j
        i, j = max(i, j), min(i, j)
    return i != j

l = 1000
rv1, rv2, tmp = [[] for x in range(l)], [[] for x in range(l)], []

for i in range(1, l):
    rv1[i] += [i]
    for j in range(i + 1, l):
        if not simulate(i, j):
            rv1[i] += [j]
            rv1[j] += [i]
            tmp += [format(int(i / math.gcd(i, j)) ^ int(j / math.gcd(i, j)), 'b')]

print(rv1)

def reduce(i, j):
    g = math.gcd(i, j)
    i /= g
    j /= g
    return int(i), int(j)

def checkAnd(i, j):
    a = format(i & j, 'b')
    return a == '1'

def checkOr(i, j): # might be nonessential but w/e
    o = format(i | j, 'b')
    return not '0' in o 

def checkXor(i, j):
    x = format(i ^ j, 'b')
    return x.count('0') == 1 and x[-1] == '0'

def invalid(i, j):
    i, j = reduce(i, j)
    return checkAnd(i, j) and checkOr(i, j) and checkXor(i, j)

for i in range(1, l):
    rv2[i] += [i]
    for j in range(i + 1, l):
        # if ((format(int(i / math.gcd(i, j)) & int(j / math.gcd(i, j)), 'b') == '1')
        #     and (not '0' in format(int(i / math.gcd(i, j)) | int(j / math.gcd(i, j)), 'b')) # might be nonessential but w/e
        #     and (format(int(i / math.gcd(i, j)) ^ int(j / math.gcd(i, j)), 'b').count('0') == 1
        #     and format(int(i / math.gcd(i, j)) ^ int(j / math.gcd(i, j)), 'b')[-1] == '0')):
        if invalid(i, j):
            rv2[i] += [j]
            rv2[j] += [i]

print(rv2)