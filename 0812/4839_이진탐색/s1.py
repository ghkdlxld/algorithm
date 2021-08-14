import sys
sys.stdin = open('sample_input.txt')


T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())


    def compare(cnt, who, P_book):
        L = P_book[0]
        R = P_book[-1]
        c = int((L + R) / 2)

        if L > R:
            return None

        if who == c:
            return cnt

        elif who < c:
            cnt += 1
            return compare(cnt, who, P_book[:int(len(P_book)/2+1)])

        else:
            cnt += 1
            return compare(cnt, who, P_book[int(len(P_book)/2-1):])



    a = compare(0, A, list(range(1, P+1)))
    b = compare(0, B, list(range(1, P+1)))

    if a < b:
        print('#{} A'.format(tc))
    elif a > b:
        print('#{} B'.format(tc))
    else:
        print('#{} 0'.format(tc))