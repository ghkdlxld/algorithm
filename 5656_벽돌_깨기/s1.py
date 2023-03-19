import sys, copy
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    bricks = [list(map(int, input().split())) for _ in range(H)]
    print(bricks)

    # 0-W 까지 열을 쭉 돌면서 dfs (curl N 회)
    # dfs 내에서 터트리고 함수1 -> 내려주기 함수2
    # 부순 벽돌 갯수 많을때마다 갱신


    # 기존 갯수 - 부순 벽돌 갯수