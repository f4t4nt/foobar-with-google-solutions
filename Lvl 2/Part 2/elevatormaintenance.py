def encode(lst):
    rv = ""
    for i in lst:
        rv += str(i) + '.'
    return rv[:-1]

def solution(lst):
    rv1 = []
    for i in lst:
        tmp = []
        tmp += map(int, i.split('.'))
        rv1 += [tmp]
    rv1.sort()
    rv2 = [encode(i) for i in rv1]
    return rv2