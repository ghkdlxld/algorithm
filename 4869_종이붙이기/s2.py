import sys
sys.stdin = open('sample_input.txt')

T = int(input())
dp = [0, 1, 3]

for tc in range(1, T+1):
    N = int(input())//10
    while N >= len(dp):
        dp.append(dp[len(dp)-2]*2 + dp[len(dp)-1])


    print('#{} {}'.format(tc, dp[N]))