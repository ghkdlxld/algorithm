import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = [0 for _ in range(10)]
    nums = list(map(int, input()))
    for n in nums:
        cnt[n] += 1

    ans = (0, 0) #번호, 장수
    for i, v in enumerate(cnt):
        if v > ans[1] or (v == ans[1] and ans[0] < i):
            ans = (i, v)


    print('#{} {} {}'.format(tc, *ans))


