n, m = map(int, input().split())

p = [0] * (n)

for _ in range(m):
    i, j, k = map(int, input().split())
    
    for l in range(i-1, j):
        p[l] = k
        


for i in p:
    print(i, end=" ")