import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    str1 = dict()
    for x in input():
        str1[x] = 0
    str2 = input()


    for s in str2:
        try:
            str1[s] += 1
        except:
            continue

    print('#{} {}'.format(tc, max(str1.values())))




