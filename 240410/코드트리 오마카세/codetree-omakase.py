import sys
from collections import deque, defaultdict

table_len, query = map(int, input().split())
table = defaultdict(lambda: defaultdict(int))
sec = 0
name_dict = {}
name_idx = 1
waiting = defaultdict(lambda: [0, 0, 0])
left_sushi = 0

def make_sushi(t, x, name):
    global table_len, left_sushi
    # t초에 위치 x에 초밥을 놓는다면
    # 테이블은 t번 오른쪽으로 회전한 이후이므로 
    # 주방장이 t만큼 왼쪽으로 회전한 테이블에 초밥이 놓인 것과 같다.
    table_idx = (x - t) % table_len
    table[table_idx][name] += 1
    left_sushi += 1

chk_queue = deque()
def check_wating(t):
    global table_len, left_sushi

    for table_idx in waiting.keys():
        _name, left, sit_time = waiting[table_idx]
        view_table_idx = (table_idx - (t - sit_time)) % table_len
        if view_table_idx not in table:
            continue
        if table[view_table_idx][_name] >= left:
            table[view_table_idx][_name] -= left
            left_sushi -= left
            chk_queue.append(table_idx)
        else:
            left_sushi -= table[view_table_idx][_name]
            left -= table[view_table_idx][_name]
            table[view_table_idx][_name] = 0
            waiting[table_idx][1] = left
    while chk_queue:
        idx = chk_queue.popleft()
        del waiting[idx] 

def come_in(t, x, n, name):
    global table_len, left_sushi

    # wating: table_idx 위치에 
    # waiting[table_idx][2] 시각부터 
    # 앉아있는 사람들 

    table_idx = (x - t) % table_len
    if table[table_idx][name] >= n:
        table[table_idx][name] -= n
        left_sushi -= n
    else:
        n -= table[table_idx][name]
        left_sushi -= table[table_idx][name]
        table[table_idx][name] = 0
        waiting[table_idx][0] = name
        waiting[table_idx][1] = n
        waiting[table_idx][2] = t

def take_pic():
    global left_sushi
    print(len(waiting), left_sushi)

for _ in range(query):
    q, *other = input().strip().split()
    if q == '100':
        t, x, name = other
        t, x = map(int, (t, x))
        if name not in name_dict:
            name_dict[name] = name_idx
            name_idx += 1
        make_sushi(t, x, name_dict[name])
        check_wating(t)
    elif q == '200':
        t, x, name, n = other
        t, x, n = map(int, (t, x, n))
        if name not in name_dict:
            name_dict[name] = name_idx
            name_idx += 1
        check_wating(t)
        come_in(t, x, n, name_dict[name])
    else:
        t = int(*other)
        check_wating(t)
        take_pic()