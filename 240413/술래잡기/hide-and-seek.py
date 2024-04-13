import sys
input = sys.stdin.readline

DEBUG = False
def parr(arr):
    if DEBUG:
        for a in arr:
            print(a)
        print()


def dbg(txt):
    if DEBUG:
        print(txt)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m, h, k = map(int, input().split())
row = col = range(n)
field = [[[set(), 0] for _ in col] for _ in row]
runner = [[-1, -1, -1]]
for i in range(1, m + 1):
    x, y, d = map(int, input().split())
    runner.append([x - 1, y - 1, d])
    field[x - 1][y - 1][0].add(i)
for _ in range(h):
    x, y = map(int, input().split())
    field[x - 1][y - 1][1] = 1

r_snail = []
hs, he, vs, ve = 0, n, 0, n
cx, cy = 0, 0
cnt = n ** 2 - 1
while cnt > 0:
    d = 2
    while cx < ve - 1:
        r_snail.append([cx, cy, d])
        cnt -= 1
        cx += 1
    d = (d - 1) % 4
    while cy < he - 1:
        r_snail.append([cx, cy, d])
        cnt -= 1
        cy += 1
    d = (d - 1) % 4
    while cx > vs:
        r_snail.append([cx, cy, d])
        cnt -= 1
        cx -= 1
    d = (d - 1) % 4
    hs += 1
    vs += 1
    he -= 1
    ve -= 1
    while cy > hs:
        r_snail.append([cx, cy, d])
        cnt -= 1
        cy -= 1

r_snail.append([n // 2, n // 2, 2])
snail = list(map(lambda x: [x[0], x[1], (x[2] + 2) % 4], r_snail))
cx, cy = n // 2, n // 2
for i in range(len(snail)):
    x, y, d = snail[i]
    if (x > cx and x == y) or (cx != x and x + y == n - 1):
        snail[i][2] = (r_snail[i][2] - 1) % 4
    if x < cx and x + 1 == y:
        snail[i][2] = (r_snail[i][2] - 1) % 4
snail.reverse()
move = [snail, r_snail]
c_idx, c_state = 0, 0

turn = 1
score = 0
remain = m
tmp = []

while k > 0 and remain > 0:
    cx, cy, cd = move[c_state][c_idx]
    dbg(f'turn {turn}')
    for i in range(1, m + 1):
        x, y, d = runner[i]
        if d == -1 or abs(cx - x) + abs(cy - y) > 3:
            continue
        dbg(f'  {i}, {runner[i]}')
        nx, ny = x + dx[d], y + dy[d]
        if nx not in row or ny not in col:
            d = (d + 2) % 4
            nx, ny = x + dx[d], y + dy[d]
        if (cx, cy) == (nx, ny):
            runner[i][2] = d
        else:
            field[x][y][0].remove(i)
            field[nx][ny][0].add(i)
            runner[i][0], runner[i][1], runner[i][2] = nx, ny, d

    c_idx += 1
    if c_idx == len(move[c_state]):
        c_state ^= 1
        c_idx = 0
    cx, cy, cd = move[c_state][c_idx]
    if field[cx][cy][1] == 0:
        score += turn * len(field[cx][cy][0])
        for s in field[cx][cy][0]:
            dbg(f'  {s} out')
            runner[s][2] = -1
            remain -= 1
        field[cx][cy][0].clear()
    for i in range(2):
        cx, cy = cx + dx[cd], cy + dy[cd]
        if cx not in row or cy not in col:
            break
        if field[cx][cy][1] == 0:
            score += turn * len(field[cx][cy][0])
            for s in field[cx][cy][0]:
                dbg(f'  {s} out')
                runner[s][2] = -1
                remain -= 1
            field[cx][cy][0].clear()
    
    turn += 1
    k -= 1
print(score)