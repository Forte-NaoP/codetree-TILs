import sys
from collections import deque

DEBUG = False

def parr(arr):
    if DEBUG:
        for a in arr:
            print(a)
        print()

def dbg(txt):
    if DEBUG:
        print(txt)

diff = [(-1, 0), (0, -1), (0, 1), (1, 0)]

n, m = map(int, input().split())
row = col = range(n)
city = [list(map(int, input().split())) for _ in row]
visit = [[0 for _ in col] for _ in row]
pos = [[-1, -1] for _ in range(m + 1)]
want = [(-1, -1)]
for _ in range(m):
    want.append(tuple(map(lambda x: int(x) - 1, input().split())))

q = deque()
def find_camp(idx, mv_num):
    x, y = want[idx]
    cx, cy, cd = 9999, 9999, 9999
    q.clear()
    q.append((x, y, 0))
    visit[x][y] = mv_num
    while q:
        x, y, d = q.popleft()
        if city[x][y] == 1:
            cd, cx, cy = min((cd, cx, cy), (d, x, y))
        for dx, dy in diff:
            nx, ny = x + dx, y + dy
            if nx not in row or ny not in col:
                continue
            if city[nx][ny] == -1 or visit[nx][ny] == mv_num:
                continue
            q.append((nx, ny, d + 1))
            visit[nx][ny] = mv_num
    return (cx, cy)

def move(idx, mv_num):
    q.clear()
    x, y = pos[idx]
    q.append((x, y, -1))
    visit[x][y] = mv_num
    while q:
        cx, cy, d = q.popleft()
        if cx == want[idx][0] and cy == want[idx][1]:
            return (x + diff[d][0], y + diff[d][1])
        for i, (dx, dy) in enumerate(diff):
            nx, ny = cx + dx, cy + dy
            if nx not in row or ny not in col:
                continue
            if city[nx][ny] == -1 or visit[nx][ny] == mv_num:
                continue
            q.append((nx, ny, d if d != -1 else i))
            visit[nx][ny] = mv_num

left = m
minute = 0
mv_idx = 999
while left > 0:
    minute += 1
    dbg(f'time: {minute}')
    for idx in range(1, min(minute + 1, m + 1)):
        if pos[idx][0] < 0:
            continue
        x, y = move(idx, mv_idx)
        dbg(f'  {idx} move {pos[idx]} to {x, y}')
        pos[idx][0], pos[idx][1] = x, y
        mv_idx += 1

    for idx in range(1, min(minute + 1, m + 1)):
        if pos[idx][0] < 0:
            continue
        if pos[idx][0] == want[idx][0] and pos[idx][1] == want[idx][1]:
            city[pos[idx][0]][pos[idx][1]] = -1
            pos[idx][0], pos[idx][1] = -2, -2
            dbg(f'  {idx} arrive at {want[idx]}')
            left -= 1
    
    if pos[min(minute, m)][0] == -1:
        cx, cy = find_camp(minute, mv_idx)
        dbg(f'  {minute} find camp {cx, cy}')
        mv_idx += 1
        pos[minute][0], pos[minute][1] = cx, cy
        city[cx][cy] = -1
    parr(city)
    
print(minute)