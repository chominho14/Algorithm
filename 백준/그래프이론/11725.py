import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())

graph = [[] for _ in range(n+1)]

parents = [0 for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph, v, parents):
    
    for i in graph[v]:
        if parents[i] == 0:
            parents[i] = v
            dfs(graph, i, parents)

dfs(graph, 1, parents)

for i in range(2, n+1):
    print(parents[i])