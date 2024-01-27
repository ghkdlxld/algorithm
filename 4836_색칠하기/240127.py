import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*10 for _ in range(10)]
    ans = 0
    for _ in range(N):
        a, b, x, y, c = map(int, input().split())
        for i in range(a, x+1):
            for j in range(b, y+1):
                if arr[i][j] == 0:
                    arr[i][j] = c
                elif arr[i][j] != c:
                    if arr[i][j] != 3:
                        ans += 1
                    arr[i][j] = 3



    print('#{} {}'.format(tc, ans))
