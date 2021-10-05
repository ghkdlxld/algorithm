import sys
sys.stdin = open('input.txt')


def make_boong():
    global s, can_sell
    for i in range(max(s) + 1):
        if i != 0 and i % M == 0:
            can_sell += K
        if sonnim[i]:
            can_sell -= sonnim[i]
            if can_sell < 0:
                return '#{} Impossible'.format(tc)
    return '#{} Possible'.format(tc)


T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    s = list(map(int, input().split()))
    can_sell = 0
    sonnim = [0]*(max(s)+1)
    for i in s:
        sonnim[i] += 1
    print(make_boong())