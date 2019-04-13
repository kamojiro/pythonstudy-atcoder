N, M = map( int, input().split())
edges = [[] for _ in range(N)]
for i in range(M):
    a, b = map( int, input().split())
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)
vertices = [ False for _ in range(N)]
ans = 0

def dfs(p):
    vertices[p] = True
    for k in edges[p]:
        if vertices[k] == False:
            dfs(k)

for i in range(N):
    if vertices[i] == False:
        dfs(i)
        ans += 1
print(ans)
