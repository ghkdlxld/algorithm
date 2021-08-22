import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))

    for i in range(len(A)-1):
        for j in range(len(A)-1-i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]


    special_sort = []

    for a in range(len(A)):
        if a%2 != 0:
            special_sort.append(A[0])
            A = A[1:]
        else:
            special_sort.append(A[-1])
            A = A[:-1]

    print('#{}'.format(tc), *special_sort[:10])
