import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    total = []
    idx = (0, M)
    while idx[1] <= N:
        tmp = sum(nums[idx[0]:idx[1]])
        total.append(tmp)
        idx = (idx[0]+1, idx[1]+1)

    print('#{} {}'.format(tc, max(total)-min(total)))