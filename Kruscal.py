from heapq import *

def find(A,x):
    p = A[x]
    if p == x:
        return x
    a = find(A,p)
    A[x] = a
    return a

def union(A, x, y):
    if find(A,x) > find(A,y):
        bx, by = find(A,y), find(A,x)
    else:
        bx, by = find(A,x), find(A,y)
    A[y] = bx
    A[by] = bx

N, M = map( int, input().split())
V = [ i for i in range(N)]
H = [(0,0,0)]*M
for i in range(M):
    s,t,w = map( int, input().split())
    H[i] = (w,s,t)
heapify(H)
ans = 0
while H:
    w,s,t = heappop(H)
    if find(V,s) != find(V,t):
        union(V,s,t)
        ans += w
print(ans)
