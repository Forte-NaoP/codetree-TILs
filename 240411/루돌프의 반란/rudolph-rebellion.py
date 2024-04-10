import sys
from collections import deque

n, m, p, r_score, s_score = map(int, input().split())
rx, ry = map(lambda x: int(x) - 1, input().split())
row = col = range(n)
r_dir = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
s_dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
santa = [[-1, -1] for _ in range(p + 1)]
score = [0 for _ in range(p + 1)]
field = [[0 for _ in col] for _ in row]
field[rx][ry] = -1
alive_santa = p

def sqr_taxi(a, b, c, d):
    return (a - c) ** 2 + (b - d) ** 2

for _ in range(p):
    si, sx, sy = map(int, input().split())
    field[sx - 1][sy - 1] = si
    santa[si][0] = sx - 1
    santa[si][1] = sy - 1

RUDOLPH_TO_SANTA = 0
SANTA_TO_RUDOLPH = 1

def interaction(si, x, y, d, i_type):
    if x not in row or y not in col:
        santa[si][0] = santa[si][1] = -1
        return
    
    nxt = field[x][y]

    santa[si][0] = x
    santa[si][1] = y
    field[x][y] = si

    if nxt == 0:
        return
    
    if i_type == RUDOLPH_TO_SANTA:
        nx, ny = x + r_dir[d][0], y + r_dir[d][1]
    else:
        nx, ny = x + s_dir[d][0], y + s_dir[d][1]
    interaction(nxt, nx, ny, d, i_type)
    
stunned = [0 for _ in range(p + 1)]
turn = 0

DEBUG = False

def dbg(txt):
    if DEBUG:
        print(txt)

def parr(arr):
    if DEBUG:
        for a in arr:
            print(a)
        print()

def collison_check(x, y, d, c_type, si = -1):
    global rx, ry, r_score, s_score, turn, alive_santa
    if c_type == RUDOLPH_TO_SANTA:
        if field[x][y] == 0:
            field[x][y], field[rx][ry] = -1, 0
            rx, ry = x, y
        else:
            target = field[x][y]
            nx = santa[target][0] + r_dir[d][0] * r_score
            ny = santa[target][1] + r_dir[d][1] * r_score 
            score[target] += r_score
            field[x][y], field[rx][ry] = -1, 0
            rx, ry = x, y
            dbg(f'rudolph to santa {target}, {target} will be {nx, ny}')
            if nx not in row or ny not in col:
                alive_santa -= 1
                santa[target][0] = santa[target][1] = -1
            else:
                stunned[target] = 2
                interaction(target, nx, ny, d, c_type)
    else:
        sx, sy = santa[si]
        if field[x][y] == 0:
            field[x][y], field[sx][sy] = si, 0
            santa[si][0] = x
            santa[si][1] = y
        else:
            dbg(f'santa {si} {sx, sy} -> {x, y} but to rudolph')
            field[sx][sy] = 0
            score[si] += s_score
            rev_d = (d + 2) % 4
            nx = x + s_dir[rev_d][0] * s_score
            ny = y + s_dir[rev_d][1] * s_score
            if nx not in row or ny not in col:
                alive_santa -= 1
                santa[si][0] = santa[si][1] = -1
                dbg(f'santa {si} out')
            else:
                stunned[si] = 1
                interaction(si, nx, ny, rev_d, c_type)

def rudolph_act():
    global rx, ry, p
    tx, ty = -1, -1
    dist = 99999
    for i in range(1, p + 1):
        sx, sy = santa[i]
        if sx == -1:
            continue
        rs = sqr_taxi(rx, ry, sx, sy)
        if rs < dist:
            dist = rs
            tx, ty = sx, sy
        elif rs == dist:
            tx, ty = max((tx, ty), (sx, sy))
    if tx == -1:
        return
    dbg(f'rudolph act to {field[tx][ty]}')
    rd = -1
    dist = 99999
    for i, (rdx, rdy) in enumerate(r_dir):
        nx, ny = rx + rdx, ry + rdy
        rs = sqr_taxi(nx, ny, tx, ty)
        if rs < dist:
            dist = rs
            rd = i
    x = rx + r_dir[rd][0]    
    y = ry + r_dir[rd][1]
    collison_check(x, y, rd, RUDOLPH_TO_SANTA)

def santa_act(si):
    global rx, ry

    if stunned[si] != 0:
        stunned[si] -= 1
        dbg(f'santa {si} stun')
        return 1

    sx, sy = santa[si]
    if sx == - 1:
        return 0
    
    dbg(f'santa {si} act')
    
    cur_dist = sqr_taxi(sx, sy, rx, ry)
    sd = -1
    for i, (dx, dy) in enumerate(s_dir):
        nx, ny = sx + dx, sy + dy
        if nx not in row or ny not in col:
            continue
        if field[nx][ny] != -1 and field[nx][ny] != 0:
            continue
        nxt_dist = sqr_taxi(nx, ny, rx, ry)
        if cur_dist > nxt_dist:
            cur_dist = nxt_dist
            sd = i

    if sd == -1:
        return 1
    x = sx + s_dir[sd][0]
    y = sy + s_dir[sd][1]
    collison_check(x, y, sd, SANTA_TO_RUDOLPH, si)
    parr(field)
    return 1

parr(field)
for _ in range(m):
    dbg(f'turn {turn}')

    rudolph_act()
    parr(field)
    acted_santa = 0
    for si in range(1, p + 1):
        acted_santa += santa_act(si)
    if acted_santa == 0:
        break

    for si in range(1, p + 1):
        if santa[si][0] == -1:
            continue
        score[si] += 1
    dbg(f'{score[1:]}')
    turn += 1

for si in range(1, p + 1):
    print(score[si], end=' ')
print()