import sys, copy
from collections import deque
sys.stdin = open('sample_input.txt')

def gravity(bricks_map):
    for w in range(W):
        for h in range(H-1, -1, -1):
            if bricks_map[h][w] == 0 and h != 0:
                x = 1
                while h-x >= 0:
                    if bricks_map[h-x][w] != 0:
                        bricks_map[h][w] = bricks_map[h-x][w]
                        bricks_map[h-x][w] = 0
                        break
                    x += 1
    # 방법 2, temp = [] 하나 해놓고 숫자 있는거만 담아서 다시 반복문 돌면서 map 재생성하는 방법


def bomb(j, bricks_map):
    cnt = 0
    q = deque()

    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]

    # 맨 위 벽돌
    for h in range(0, H):
        if bricks_map[h][j] != 0:
            q.append((h, j))
            break

    while q:
        bomb_i, bomb_j = q.popleft()


        if bricks_map[bomb_i][bomb_j] != 1:
            for k in range(4):
                d = 1
                while d < bricks_map[bomb_i][bomb_j]:
                    ni, nj = bomb_i + di[k]*d, bomb_j + dj[k]*d
                    if 0 <= ni < H and 0 <= nj < W and bricks_map[ni][nj] != 0 and (ni, nj) not in q:
                        q.append((ni, nj))
                    d += 1
        bricks_map[bomb_i][bomb_j] = 0
        cnt += 1

    gravity(bricks_map)

    return cnt



def dfs(curl, cnt, bricks_map):
    global bomb_bricks, N

    if curl == N:
        if cnt > bomb_bricks:
            bomb_bricks = cnt
        return


    for w in range(W):
        tmp_bricks = copy.deepcopy(bricks_map)
        break_cnt = bomb(w, bricks_map)
        dfs(curl + 1, cnt + break_cnt, bricks_map)
        bricks_map = tmp_bricks



T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    bricks_map = []
    bricks_num = 0  # 벽돌 갯수
    bomb_bricks = 0 # 터뜨린 갯수

    for k in range(H):

        brick = list(map(int, input().split()))
        bricks_map.append(brick)
        bricks_num += (W - brick.count(0))

    if bricks_num != 0:
        dfs(0, 0, bricks_map)

    print('#{} {}'.format(tc, bricks_num-bomb_bricks))