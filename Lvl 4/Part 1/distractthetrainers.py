def gcd(i, j):
    while j:
        i, j = j, i % j
    return i

def reduce(i, j):
    g = gcd(i, j)
    i //= g
    j //= g
    return i, j

def check_and(i, j):
    a = format(i & j, 'b')
    return a == '1'

def check_or(i, j): # might be nonessential but w/e
    o = format(i | j, 'b')
    return not '0' in o 

def check_xor(i, j):
    x = format(i ^ j, 'b')
    return x.count('0') == 1 and x[-1] == '0'

def invalid(i, j):
    i, j = reduce(i, j)
    return check_and(i, j) and check_or(i, j) and check_xor(i, j)

# curr_min = 100

# def recurse(ref, visited, i, curr_val):
#     global curr_min
#     if curr_val == len(ref) % 2:
#         return curr_val
#     elif curr_val + i - len(ref) >= curr_min:
#         return 100
#     elif i == len(ref):
#         curr_min = curr_val
#         return curr_val
#     elif visited[i]:
#         return recurse(ref, visited, i + 1, curr_val)
#     else:
#         ret_val = curr_val
#         visited[i] = True
#         for j in ref[i]:
#             if not visited[j]:
#                 visited[j] = True
#                 ret_val = min(ret_val, recurse(ref, visited, i + 1, curr_val - 2))
#                 if ret_val == len(ref) % 2:
#                     return len(ref) % 2
#                 visited[j] = False
#         visited[i] = False
#         ret_val = min(ret_val, recurse(ref, visited, i + 1, curr_val))
#         return ret_val

def greedy(ref):
    deg, paired = [], { -1 }
    for i in range(len(ref)):
        if len(ref[i]) > 0:
            deg += [(len(ref[i]), i)]
    deg.sort()
    for i in range(len(deg)):
        x = deg[i][1]
        if x in paired:
            continue
        else:
            y = (100, -1)
            for j in ref[x]:
                if j in paired:
                    continue
                else:
                    if y[0] >= len(ref[j]):
                        y = (len(ref[j]), j)
            if y != (100, -1):
                paired.add(x)
                paired.add(y[1])
    return (len(ref) - len(paired) + 1)

def solution(banana_list):
    ref = [[] for i in range(len(banana_list))]
    for i in range(len(banana_list)):
        for j in range(i + 1, len(banana_list)):
            if not invalid(banana_list[i], banana_list[j]):
                ref[i] += [j]
                ref[j] += [i]
    # return recurse(ref, [False for i in range(len(ref))], 0, len(ref)) # timeout
    return greedy(ref)

# def convert(x, ref):
#     for i in reversed(range(len(ref))):
#         if x % ref[i] == 0:
#             return i
#     return -1

# def solution(banana_list):
#     ref, idx_list, idx_set, rv = [1], [0] * 29, [], 0
#     for i in range(29):
#         ref += [ref[-1] * 2 + 1]
#     for i in banana_list:
#         idx_list[convert(i, ref)] += 1
#     for i in idx_list:
#         if i > 0:
#             idx_set += [i]
#     while len(idx_set) > 1:
#         idx_set.sort()
#         max1 = idx_set[-1]
#         idx_set = idx_set[:-1]
#         max2 = idx_set[-1]
#         idx_set = idx_set[:-1]
#         if max1 > max2:
#             idx_set += [max1 - max2]
#     if len(idx_set) == 1:
#         rv = idx_set[0]
#     return rv