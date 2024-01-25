import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split())) #충전소
    stop = [1]+[0 for _ in range(N)]
    now = 0
    ans = 0

    now += K
    while now < N:
        if now in charge and stop[now] != 1:
            stop[now] = 1
            ans += 1
            now += K

        elif stop[now] == 0:
            now -= 1

        else:
            ans = 0
            break



    print('#{} {}'.format(tc, ans))
