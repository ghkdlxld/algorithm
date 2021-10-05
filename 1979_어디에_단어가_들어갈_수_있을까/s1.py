import sys
sys.stdin = open('input.txt')

def check(puzzle):
    cnt = 0
    for i in puzzle:
        for x in range(len(i)-K-1):
            if i[x:x+K+2] == ['0']+['1']*K+['0']:
                cnt += 1
    return cnt

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [['0']*(N+2)] + [['0'] + input().split() + ['0'] for _ in range(N)] + [['0']*(N+2)]


    # 가로
    a = check(puzzle)

    # 세로
    for i in range(N+2):
        for j in range(N+2):
            if i < j:
                puzzle[i][j], puzzle[j][i] = puzzle[j][i], puzzle[i][j]

    b = check(puzzle)

    print('#{} {}'.format(tc, a+b))