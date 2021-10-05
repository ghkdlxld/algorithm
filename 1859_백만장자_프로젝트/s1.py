import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 날짜 수
    price = list(map(int, input().split()))[-1::-1] # 거꾸로 정렬

    max_p = price[0]
    benefit = 0

    for p in range(len(price)-1):
        if max_p > price[p+1]:
            benefit += max_p-price[p+1]

        else:
            max_p = price[p+1]

    print('#{} {}'.format(tc, benefit))


