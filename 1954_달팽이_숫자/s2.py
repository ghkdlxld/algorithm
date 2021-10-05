import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    for arr_a in range(N):
        arr.append([0]*N)


    # 우 하 좌 상
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]


    # 처음 시작 위치
    i, j = 0, -1

    cnt = 1
    k = 0
    while cnt <= N*N:
        ni = i + di[k]  # 오른쪽으로 이동
        nj = j + dj[k]

        if (0 <= ni < N) and (0 <= nj < N) and arr[ni][nj] == 0:
            arr[ni][nj] = cnt
            cnt += 1
            i, j = ni, nj

        else:   # 방향을 바꿈
            k = (k+1) % 4

    print('#{}'.format(tc))
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')
        print()








