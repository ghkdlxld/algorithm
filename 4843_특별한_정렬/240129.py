import sys
sys.stdin = open('sample_input.txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = sorted(list(map(int, input().split())), reverse=True)
    ans = []
    for i in range(5):
        ans.append(arr[i])
        ans.append(arr[-(i+1)])

    print('#{}'.format(tc), *ans)
