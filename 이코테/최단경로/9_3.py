# 전보
import heapq
INF = int(1e9)

n, m, c = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

distance = [INF]*(n+1)    

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if  cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
dijkstra(c)

cnt = 0
max_distance = 0

for i in distance:
    if i != INF:
        cnt += 1
        max_distance = max(max_distance, i)
        
print(cnt - 1, max_distance)
    

