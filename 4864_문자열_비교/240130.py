import sys
sys.stdin = open('sample_input.txt')



T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    ans = 0

    def compare(idx):
        for a in str1:
            if idx >= len(str2):
                return False
            elif a == str2[idx]:
                idx += 1
            else:
                return False
        return True

    for i, b in enumerate(str2):
        if b == str1[0]:
            if compare(i):
                ans = 1
                break

    print('#{} {}'.format(tc, ans))