import sys, copy
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    bricks = [list(map(int, input().split())) for _ in range(H)]
    print(bricks)


    def brick_break(start, arr):
        cnt = [0, 0] # idx, 부순 갯수 (max)
        # 0-W 길이만큼 순회하면서 부순 갯수 세기
        for w in range(W):
            pass

    for n in range(N): # 시작점
        brick_break(0, n, copy.deepcopy(bricks))
