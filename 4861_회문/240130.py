import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]


    # 회문 찾는 함수 ( 가로만 비교 )
    def find():
        pass



# arr 에서 한번 찾은후,
# arr 뒤집어서 한번더 체크
