import sys
from collections import deque
from copy import deepcopy

DEBUG = False

def parr(arr):
    if DEBUG:
        for a in arr:
            print(a)
        print()

def dbg(txt):
    if DEBUG:
        print(txt)

def rotate(x, y, s, px, py):
    x, y = x - px, y - py
    x, y = y, s - 1 - x
    x, y = x + px, y + py
    return x, y

def left_up_square(rx, ry, ex, ey):
    mx, my = min(rx, ex), min(ry, ey)
    Mx, My = max(rx, ex), max(ry, ey)

    size = max(Mx - mx, My - my) + 1

    sx = max(0, mx - max(0, size - (Mx - mx + 1)))
    sy = max(0, my - max(0, size - (My - my + 1)))

    return size, sx, sy

n, m, k = map(int, input().split())
row = col = range(n)
maze = [list(map(int, input().split())) for _ in row]
maze_copy = deepcopy(maze)
runner = []
for i in range(1, m + 1):
    runner.append(list(map(lambda x: int(x) - 1, input().split())))
ex, ey = map(lambda x: int(x) - 1, input().split())
diff = [(-1, 0), (1, 0), (0, -1), (0, 1)]

move_dist = 0
remain_runner = m
while k > 0 and remain_runner > 0:
    s, sx, sy = 11, 11, 11
    dbg(f'{k} sec left')
    for i in range(m):
        rx, ry = runner[i]
        if rx == -1:
            continue
        exit_dist = abs(rx - ex) + abs(ry - ey)
        for dx, dy in diff:
            nx, ny = rx + dx, ry + dy
            if nx not in row or ny not in col or maze[nx][ny] > 0:
                continue
            nxt_dist = abs(nx - ex) + abs(ny - ey)
            if nxt_dist < exit_dist:
                move_dist += 1
                if nxt_dist == 0:
                    runner[i][0] = runner[i][1] = -1
                    remain_runner -= 1
                    dbg(f'    runner {i} exit')
                else:
                    runner[i][0], runner[i][1] = nx, ny
                    dbg(f'    runner {i} to {nx, ny}')
                break
        rx, ry = runner[i]
        if rx == -1:
            continue
        ts, tsx, tsy = left_up_square(rx, ry, ex, ey)
        if s > ts:
            s, sx, sy = ts, tsx, tsy
        elif s == ts:
            sx, sy = min((sx, sy), (tsx, tsy))
        dbg(f'    sqr update with {i}({rx, ry}, {ex, ey}) {sx, sy} {s}')
    if remain_runner == 0:
        break
    dbg(f'  square {sx, sy}, {s}')
    for i in range(s):
        for j in range(s):
            maze[sx + j][sy + s - 1 - i] = max(maze_copy[sx + i][sy + j] - 1, 0)
    for i in range(s):
        for j in range(s):
            maze_copy[i + sx][j + sy] = maze[i + sx][j + sy]

    ex, ey = rotate(ex, ey, s, sx, sy)
    
    for i in range(m):
        rx, ry = runner[i]
        if rx not in range(sx, sx + s) or ry not in range(sy, sy + s):
            continue
        runner[i][0], runner[i][1] = rotate(rx, ry, s, sx, sy)
    dbg(f'  exit {ex, ey}')
    dbg(f'  {runner}')
    parr(maze)
    k -= 1
print(move_dist)
print(ex + 1, ey + 1)