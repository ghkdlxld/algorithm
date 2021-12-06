from collections import deque
from itertools import combinations


def move_time(si, sj, pi, pj):
    return abs(pi - si) + abs(pj - sj)


def make_s2(s1):
    return ppl_num - s1


def match_ppl(x):
    return move_s1_s2[x]


# 사람수(1~10), N(4~10) 계단입구 2개
T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 방 한변의 길이
    room = [list(map(int, input().split())) for _ in range(N)]
    stair = []
    ppl = []
    for i in range(N):
        for j in range(N):
            if room[i][j] == 1:
                ppl.append([i, j])
            elif room[i][j] != 0:
                stair.append([room[i][j], i, j])  # 계단길이, si, sj

    move_s1_s2 = []
    for i in ppl:
        s1 = move_time(*stair[0][1:], *i)
        s2 = move_time(*stair[1][1:], *i)
        move_s1_s2.append([s1, s2])

    s1 = deque()  # 계단 1로 간 사람들
    s2 = deque()  # 계단 2로 간 사람들

    ppl_num = set(range(len(ppl)))
    for i in range(0, len(ppl) + 1):
        pick = list(map(set, combinations(ppl_num, i)))
        s1.extend(pick)
        pick2 = list(map(make_s2, pick))
        s2.extend(pick2)

    result = 99999
    for _ in range(len(s1)):
        a = s1.popleft()
        b = s2.popleft()
        a = deque(map((lambda x: x[0]), sorted(map(match_ppl, a), key=lambda x: x[0])))
        b = deque(map((lambda x: x[1]), sorted(map(match_ppl, b), key=lambda x: x[1])))
        stair_a = deque()
        stair_b = deque()
        out = 0
        time = 0
        while out != len(ppl):
            time += 1
            if len(stair_a) != 0:
                stair_a = deque(map((lambda x: x - 1), stair_a))
                while len(stair_a) != 0 and stair_a[0] == 0:
                    stair_a.popleft()
                    out += 1
            if len(a) != 0:
                a = deque(map((lambda x: x - 1), a))
                while len(a) != 0 and a[0] <= 0 and len(stair_a) != 3:
                    a.popleft()
                    stair_a.append(stair[0][0])

            if len(stair_b) != 0:
                stair_b = deque(map((lambda x: x - 1), stair_b))
                while len(stair_b) != 0 and stair_b[0] == 0:
                    stair_b.popleft()
                    out += 1
            if len(b) != 0:
                b = deque(map((lambda x: x - 1), b))
                while len(b) != 0 and b[0] <= 0 and len(stair_b) != 3:
                    b.popleft()
                    stair_b.append(stair[1][0])
        if time < result:
            result = time

    print('#{} {}'.format(tc, result + 1))