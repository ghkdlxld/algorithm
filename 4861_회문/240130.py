import sys, copy
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]


    def find(lst):
        for i in range(N):
            for j in range(N - M + 1):
                words = ''.join(lst[i][j:j + M])
                sdrow = words[::-1]
                if words == sdrow:
                    return words
        return False


    ans = find(arr)
    if ans:
        print('#{} {}'.format(tc, ans))

    else:
        arr_rev = copy.deepcopy(arr)
        for a in range(N):
            for b in range(N):
                arr_rev[a][b] = arr[b][a]

        print('#{} {}'.format(tc, find(arr_rev)))






