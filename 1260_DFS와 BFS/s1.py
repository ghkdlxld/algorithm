import sys
sys.stdin = open('input.txt')


def DFS(V):
    stack = []
    stack.append(V)
    visited[V] = 1

    while stack:
        t = stack.pop(0)
        print(t, end=' ')
        for v in link[t]:
            if visited[v] == 0:
                DFS(v)


def BFS(V):
    que = [start]
    visited[V] = 1

    while que:
        t = que.pop(0)
        print(t, end=' ')
        for v in link[t]:
            if visited[v] == 0:
                visited[v] = 1
                que.append(v)


node, line, start = map(int, input().split())
x = [[] for _ in range(node+1)]
for i in range(line):
    a, b = map(int, input().split())
    x[a].append(b)
    x[b].append(a)
link = []
for y in x:
    link.append(sorted(y))
visited = [0]*(node+1)
DFS(start)
print()
visited = [0]*(node+1)
BFS(start)