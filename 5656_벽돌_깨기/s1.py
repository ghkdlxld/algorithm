import sys, copy
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    bricks = [list(map(int, input().split())) for _ in range(H)]
    print(bricks)


    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]

    def dfs(w, curl):
        if curl == 3:
            return

        # w 열에서 가장 윗 자리 찾아서 터트리기
        for h in range(H):
            if bricks[h][w] != 0:
                # 터트리기

                break

    # dfs 내에서 터트리고 함수1 -> 내려주기 함수2


    # 0-W 까지 열을 쭉 돌면서 dfs (curl N 회)
    for j in range(W):
        dfs(j, 0)


    # 부순 벽돌 갯수 많을때마다 갱신


    # 기존 갯수 - 부순 벽돌 갯수