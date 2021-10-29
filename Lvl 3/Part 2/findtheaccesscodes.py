def solution(l):
    rv, ref = 0, [[] for i in range(len(l))]
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[j] % l[i] == 0:
                ref[i] += [j]
    for i in range(len(l)):
        for j in ref[i]:
            rv += len(ref[j])
    return rv

# def solution(l):
#     rv = 0
#     for i in range(len(l)):
#         for j in range(i + 1, len(l)):
#             if l[j] % l[i] == 0:
#                 for k in range(j + 1, len(l)):
#                     if l[k] % l[j] == 0:
#                         rv += 1
#     return rv