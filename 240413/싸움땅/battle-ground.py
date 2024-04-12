import sys
from collections import deque
import heapq

hpush = heapq.heappush
hpop = heapq.heappop
hpp = heapq.heappushpop

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
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m, k = map(int, input().split())
row = col = range(n)
field = [[[-1, []] for _ in col] for _ in row]
for i in row:
    for j, v in enumerate(map(int, input().split())):
        if v != 0:
            hpush(field[i][j][1], -v)

user = []
score = [0 for _ in range(m)]

for i in range(m):
    x, y, d, s = map(int, input().split())
    field[x - 1][y - 1][0] = i
    user.append([x - 1, y - 1, d, -s, 0])

def win(a, point):
    score[a] += point
    x, y = user[a][0], user[a][1]
    if user[a][4] != 0:
        hpush(field[x][y][1], user[a][4])
    if field[x][y][1]:
        user[a][4] = hpop(field[x][y][1])
    field[x][y][0] = a

def lose(a):
    x, y, d = user[a][0], user[a][1], user[a][2]
    if user[a][4] != 0:
        hpush(field[x][y][1], user[a][4])
        user[a][4] = 0
    
    while True:
        nx, ny = x + dx[d], y + dy[d]
        if nx not in row or ny not in col or field[nx][ny][0] != -1:
            d = (d + 1) % 4
        else:
            user[a][0], user[a][1], user[a][2] = nx, ny, d
            win(a, 0)
            break

def fight(a, b):
    pa = user[a][3] + user[a][4]
    pb = user[b][3] + user[b][4]
    score = abs(pa - pb)
    if pa != pb:
        (lose(a), win(b, score)) if pa > pb else (lose(b), win(a, score))
    else:
        (lose(a), win(b, score)) if user[a][3] > user[b][3] else (lose(b), win(a, score))


def move(a):
    x, y, d = user[a][0], user[a][1], user[a][2]
    nx, ny = x + dx[d], y + dy[d]
    if nx not in row or ny not in col:
        d = (d + 2) % 4
        nx, ny = x + dx[d], y + dy[d]
    field[x][y][0] = -1
    user[a][0], user[a][1], user[a][2] = nx, ny, d
    return (nx, ny, d)

while k > 0:
    for i in range(m):
        x, y, d = move(i)
        if field[x][y][0] == -1:
            win(i, 0)
        else:
            fight(i, field[x][y][0])
    k -= 1

print(*score)