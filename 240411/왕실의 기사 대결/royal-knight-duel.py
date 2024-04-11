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

diff = [(-1, 0), (0, 1), (1, 0), (0, -1)]

map_size, knight_num, order_cnt = map(int, input().split())
row = col = range(map_size)
chess = [list(map(int, input().split())) for _ in row]
knight = []
knight_hp = []

for _ in range(knight_num):
    x, y, h, w, hp = map(int, input().split())
    knight.append([x - 1, y - 1, h, w])
    knight_hp.append([hp, 0])

trap = list(map(lambda x: list(map(lambda y: 0 if y == 2 else y, x)), chess))
# 함정은 누적합으로 미리 계산
for i in row:
    for j in range(1, map_size):
        trap[i][j] += trap[i][j - 1]
for j in col:
    for i in range(1, map_size):
        trap[i][j] += trap[i - 1][j]

def get_trap_cnt(x1, y1, x2, y2):
    total = trap[x2][y2]
    if y1 > 0:
        total -= trap[x2][y1 - 1]
    if x1 > 0:
        total -= trap[x1 - 1][y2]
    if x1 > 0 and y1 > 0:
        total += trap[x1 - 1][y1 - 1]
    return total

dmg_queue = deque()

CANNOT_MOVE = False
CAN_MOVE = True

def collision_check(x, y, a, b, c, d):
    return a <= x < a + c and b <= y < b + d

def order(k, d, dmg_chk = False):
    x, y, h, w = knight[k]
    chk_set = set()

    if d % 2 == 0: # up, down
        nx = (x if d == 0 else x + h - 1 ) + diff[d][0]
        if nx not in row:
            return CANNOT_MOVE
        s, e = y, y + w
    else: # left, right
        ny = (y if d == 3 else y + w - 1 ) + diff[d][1]
        if ny not in col:
            return CANNOT_MOVE
        s, e = x, x + h

    for i in range(s, e):
        nx, ny = (nx, i) if d % 2 == 0 else (i, ny)
        # 다음 칸에 벽이 하나라도 있으면
        if chess[nx][ny] == 2:
            return CANNOT_MOVE
        
    for i in range(s, e):
        nx, ny = (nx, i) if d % 2 == 0 else (i, ny)  
        for idx, info in enumerate(knight):
            if idx == k: # 자기 자신 제외
                continue
            if knight_hp[idx][0] == knight_hp[idx][1]: # 죽은 기사 제외
                continue
            if collision_check(nx, ny, *info):
                chk_set.add((idx, d))
    # 이동할 칸이 전부 빈칸이면
    if not chk_set:
        if dmg_chk:
            dmg_queue.append((k, d))
        return CAN_MOVE

    result = CAN_MOVE
    for idx, d in chk_set:
        result &= order(idx, d, True)

    return result

def dmg_calculate():
    while dmg_queue:
        i, d = dmg_queue.popleft()
        x, y, h, w = knight[i]
        x += diff[d][0]
        y += diff[d][1]
        knight[i][0] = x
        knight[i][1] = y
        trap_cnt = get_trap_cnt(x, y, x + h - 1, y + w - 1)
        knight_hp[i][1] += trap_cnt
        dbg(f'  knight {i} move {d} and hit {trap_cnt} dmg')

for _ in range(order_cnt):
    i, d = map(int, input().split())
    dbg(f'order {i} {d}')
    if knight_hp[i - 1][0] == knight_hp[i - 1][1]:
        continue
    if order(i - 1, d) == CAN_MOVE:
        knight[i - 1][0] += diff[d][0]
        knight[i - 1][1] += diff[d][1]
        dmg_calculate()
        parr(knight)

parr(knight_hp)
ans = 0
for max_hp, get_dmg in knight_hp:
    ans += get_dmg if max_hp > get_dmg else 0

print(ans)