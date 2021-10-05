import sys
sys.stdin = open('input.txt')

# bubble sort
T = int(input())
for tc in range(1, T+1):
    N = input()
    nums = list(map(int, input().split()))

    for i in range(len(nums)-1):
        for j in range(len(nums)-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]


    interval = nums[-1] - nums[0]

    print('#{} {}'.format(tc, interval))
