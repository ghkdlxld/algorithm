import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())

    def cnt_page(x, l, r):
        cnt = 0
        while True:
            c = int((l+r)/2)
            if x == c:
                cnt += 1
                return cnt
            else:
                if x < c:
                    r = c
                    cnt += 1
                else:
                    l = c
                    cnt += 1


    if cnt_page(A, 1, P) < cnt_page(B, 1, P):
        print("#{} {}".format(tc, "A"))
    elif cnt_page(A, 1, P) > cnt_page(B, 1, P):
        print("#{} {}".format(tc, "B"))
    else:
        print("#{} {}".format(tc, 0))