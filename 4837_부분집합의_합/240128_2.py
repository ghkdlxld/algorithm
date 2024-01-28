import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = list(range(1, 13))  # A = 1~12
    ans = 0

    for i in range(1<<12): # 12개의 원소가 포함되느냐 1 / 안되느냐 0 -> 총 2**12번 반복
        tmp = []
        for j in range(12): # 12개의 원소를 돌면서 탐색
            if i&(1<<j): # 포함되면 (ex i: 0~2**12 => 000000000000 ~ 111111111111 / 1<<j : 2**j 둘이 같으면 -> j번째 원소는 포함인걸로 체크)
                tmp.append(A[j])

        if len(tmp) == N and sum(tmp) == K: # 이때 이진수 i에 1이 세번 들어가는 숫자일때를 체크 (tmp에 2**j가 세번 들어갔을 것임)
            ans += 1



    print('#{} {}'.format(tc, ans))
