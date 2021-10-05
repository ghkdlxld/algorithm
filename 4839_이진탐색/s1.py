import sys
sys.stdin = open('sample_input.txt')


def compare(L, R, who, cnt):
    c = int((L + R) / 2)

    if who == c:
        return cnt

    elif who < c:
        cnt += 1
        return compare(L, c, who, cnt)

    else:
        cnt += 1
        return compare(c, R, who, cnt)


T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())

    a = compare(1, P, A, 0)
    b = compare(1, P, B, 0)

    if a < b:
        print('#{} A'.format(tc))
    elif a > b:
        print('#{} B'.format(tc))
    else:
        print('#{} 0'.format(tc))