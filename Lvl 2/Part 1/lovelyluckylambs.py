def maxMen(total_lambs):
    rv, curr_lambs, prev_lambs, given_lambs = 1, 1, 0, 0
    while total_lambs >= given_lambs:
        given_lambs += curr_lambs
        tmp = curr_lambs
        curr_lambs += prev_lambs
        prev_lambs = tmp
        rv += 1
    return rv

def minMen(total_lambs):
    rv, curr_lambs, given_lambs = 1, 1, 0
    while total_lambs >= given_lambs:
        given_lambs += curr_lambs
        curr_lambs *= 2
        rv += 1
    return rv

def solution(total_lambs):
    return maxMen(total_lambs) - minMen(total_lambs)