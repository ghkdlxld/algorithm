import sys
sys.stdin = open('sample_input.txt')

def way_idx(num):
    num = (num+1)//2
    return num


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    way = [0] * 201

    students = []
    for _ in range(N):
        student = list(map(int, input().split()))
        students.append(student)

    for s in students:
        if s[0] > s[1]:
            s[0], s[1] = s[1], s[0]


    students_way = []
    for i in range(len(students)):
        students_way.append(list(map(way_idx, students[i])))

    for a in range(N):
        x = students_way[a][0]
        while x <= students_way[a][1]:
            way[x] += 1
            x += 1

    print('#{} {}'.format(tc, max(way)))
