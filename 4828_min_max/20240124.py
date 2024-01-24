import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int,(input().split())))
    max_num = max(A)
    min_num = min(A)

    print('#{} {}'.format(tc, max_num-min_num))