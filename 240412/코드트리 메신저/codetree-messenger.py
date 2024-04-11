import sys
from collections import deque
from copy import deepcopy

DEBUG = True

def parr(arr):
    if DEBUG:
        for a in arr:
            print(a)
        print()

def dbg(txt):
    if DEBUG:
        print(txt)

room_cnt, query_cnt = map(int, input().split())
room = [[-1, -1, -1] for _ in range(room_cnt + 1)]
power = [0 for _ in range(room_cnt + 1)]
state = [True for _ in range(room_cnt + 1)]
init = list(map(int, input().split()))

for i in range(1, room_cnt + 1):
    p = init[i]
    room[i][0] = p
    if room[p][1] == -1:
        room[p][1] = i
    else:
        room[p][2] = i

power[1:] = init[room_cnt + 1:]

def propagation(room_idx, depth):
    val = 0
    if not state[room_idx]:
        return val
    
    if power[room_idx] >= depth:
        val += 1
    if room[room_idx][1] != -1:
        val += propagation(room[room_idx][1], depth + 1)
    if room[room_idx][2] != -1:
        val += propagation(room[room_idx][2], depth + 1)
    return val

for _ in range(query_cnt - 1):
    query = list(map(int, input().split()))
    if query[0] == 200:
        state[query[1]] ^= True
    elif query[0] == 300:
        power[query[1]] = query[2]
    elif query[0] == 400:
        c1, c2 = query[1], query[2]
        c1_p, c2_p = room[c1][0], room[c2][0]
        if c1_p == c2_p:
            continue
        room[c1][0], room[c2][0] = c2_p, c1_p
        if room[c1_p][1] == c1:
            room[c1_p][1] = c2
        else:
            room[c1_p][2] = c2
        
        if room[c2_p][1] == c2:
            room[c2_p][1] = c1
        else:
            room[c2_p][2] = c1
    elif query[0] == 500:
        state_bak = state[query[1]]
        state[query[1]] = True
        print(propagation(query[1], 0) - 1)
        state[query[1]] = state_bak