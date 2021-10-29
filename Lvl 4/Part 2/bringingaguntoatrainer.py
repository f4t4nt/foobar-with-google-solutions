import math

def dist_pos(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)

def reflect(positions, x = None, y = None): # x = X != 0 means reflect over x = X, same for y
    rv = []
    for pos in positions:
        nv = pos
        if x != None:
            nv = [[2 * x - nv[0], nv[1]]]
        if y != None:
            nv = [[nv[0], 2 * y - nv[1]]]
        rv += nv
    return rv

def contains(pos1, pos2, pos3): # obsolete due to using angles
    return dist_pos(pos3, pos1) + dist_pos(pos3, pos2) == dist_pos(pos1, pos2)

# ...     ...     ...     ...    ...    ...   ...
# ...    3,-2    3,-1    3, 0   3, 1   3, 2   ...
# ...    2,-2    2,-1    2, 0   2, 1   2, 2   ...
# ...    1,-2    1,-1    1, 0   1, 1   1, 2   ...
# ...    0,-2    0,-1    0, 0   0, 1   0, 2   ...
# ...   -1,-2   -1,-1   -1, 0  -1, 1  -1, 2   ...
# ...   -2,-2   -2,-1   -2, 0  -2, 1  -2, 2   ...
# ...   -3,-2   -3,-1   -3, 0  -3, 1  -3, 2   ...
# ...     ...     ...     ...    ...    ...   ...

def solution(dimensions, my_pos, train_pos, distance):
    if dist_pos(my_pos, train_pos) > distance:
        return 0
    x_dim, y_dim, omx, omy, otx, oty, ref, visited, bfs, rv = dimensions[0], dimensions[1], my_pos[0], my_pos[1], train_pos[0], train_pos[1], { (0, 0): (my_pos, train_pos) }, { (0, 0) }, [ (1, 0), (-1, 0), (0, 1), (0, -1) ], 1
    ref[(1, 0)] = reflect(ref[(0, 0)], y = y_dim)
    ref[(-1, 0)] = reflect(ref[(0, 0)], y = 0)
    ref[(0, 1)] = reflect(ref[(0, 0)], x = x_dim)
    ref[(0, -1)] = reflect(ref[(0, 0)], x = 0)
    angles = { math.atan2(oty - omy, otx - omx) }
    while len(bfs) > 0:
        curr_ref = bfs[0]
        i, j = curr_ref[0], curr_ref[1]
        bfs = bfs[1:]
        if curr_ref in visited:
            continue
        visited.add(curr_ref)
        curr_my_pos, curr_train_pos = ref[curr_ref][0], ref[curr_ref][1]
        cmx, cmy, ctx, cty = curr_my_pos[0], curr_my_pos[1], curr_train_pos[0], curr_train_pos[1]
        dx, dy = cmx - omx, cmy - omy
        angles.add(math.atan2(dy, dx))
        correct_distance = dist_pos(my_pos, curr_train_pos) <= distance
        if correct_distance:
            dx, dy = ctx - omx, cty - omy
            angle = math.atan2(dy, dx)
            if not angle in angles:
                angles.add(angle)
                rv += 1
            ref[(i + 1, j)] = reflect(ref[curr_ref], y = (i + 1) * y_dim)
            ref[(i - 1, j)] = reflect(ref[curr_ref], y = i * y_dim)
            ref[(i, j + 1)] = reflect(ref[curr_ref], x = (j + 1) * x_dim)
            ref[(i, j - 1)] = reflect(ref[curr_ref], x = j * x_dim)
            if not (i + 1, j) in visited:
                bfs += [(i + 1, j)]
            if not (i - 1, j) in visited:
                bfs += [(i - 1, j)]
            if not (i, j + 1) in visited:
                bfs += [(i, j + 1)]
            if not (i, j - 1) in visited:
                bfs += [(i, j - 1)]
            # bfs += [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
    return rv