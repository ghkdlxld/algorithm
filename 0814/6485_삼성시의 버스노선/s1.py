import sys
sys.stdin = open('s_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 노선 수

    line_bus_stop = []
    for n in range(N):
        A, B = map(int, input().split())
        for ab in range(A, B+1):
            line_bus_stop.append(ab)

    P = int(input())    # 노선 개수 구하고자 하는 버스 정류장 수
    bus_stop_lst = []
    for p in range(P):
        bus_stop_num = int(input()) # 버스 정류장 번호
        bus_stop_lst.append(bus_stop_num)


    bus_cnt = []
    for bus in bus_stop_lst:
        cnt = 0
        for num in line_bus_stop:
            if num == bus:
                cnt += 1
        bus_cnt.append(cnt)

    print('#{}'.format(tc), *bus_cnt)
