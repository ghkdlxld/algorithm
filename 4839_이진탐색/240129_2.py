import sys
sys.stdin = open('sample_input.txt')


def cnt_page(x, l, r, cnt):
    c = int((l + r) / 2)
    if x == c:
        return cnt
    else:
        if x < c:
            return cnt_page(x, l, c, cnt + 1)
        else:
            return cnt_page(x, c, r, cnt + 1)



T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())

    a = cnt_page(A, 1, P, 0)
    b = cnt_page(B, 1, P, 0)

    if a<b:
        print("#{} {}".format(tc, "A"))
    elif a>b:
        print("#{} {}".format(tc, "B"))
    else:
        print("#{} {}".format(tc, 0))
