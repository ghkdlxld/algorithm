import sys
from collections import deque
sys.stdin = open('sample_input.txt')



T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    bricks = [list(map(int, input().split())) for _ in range(H)]
    print(bricks)

    # 벽돌 떨어뜨리기 N 회 * range(0, W) -> 터뜨린 갯수는 range 단위마다 계산
    # 떨어뜨릴 w 위치 정하고, 가장 위 벽돌탐지 -> 터뜨릴 벽돌 q?나 갯수 count , -1 표시(중복x)
    # curl == N 모든 벽돌 떨어뜨리거나, 더이상 터뜨릴 벽돌이 없다면(q가 비었을 경우 or count == 0) continue, ans 최댓값이랑 비교 교체

    # 터뜨릴 돌 다 count 했으면 gravity (w 만큼 돌면서 맨 위 벽돌이 0 이 아닐경우 -1 된 곳은 0으로, 맨위 는 아래로 / 만약 맨위가 0이면 -1 다 0으로)

    # 주의 : 다음 경우의수로 들어갈때 이전거 되돌리려면 copy로 넣어서 계산 및 count 재설정 고려!!!!