import sys
from itertools import combinations
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = list(range(1, 13))
    ans = 0
    group = list(combinations(A, N))
    for g in group:
        if sum(g) == K:
            ans += 1

    print('#{} {}'.format(tc, ans))