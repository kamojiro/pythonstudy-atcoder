# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_5_A&lang=jp
def diameter(N, E, D):#diamete of a tree
    from collections import deque
    V = [-1]*N
    V[0] = 0
    q = deque([0])
    while q:
        v = q.popleft()
        for w in E[v]:
            if V[w] == -1:
                V[w] = V[v] + D[(v,w)]
                q.append(w)
    s = V.index( max(V))
    p = deque([s])
    W = [-1]*N
    W[s] = 0
    while p:
        v = p.popleft()
        for w in E[v]:
            if W[w] == -1:
                W[w] = W[v] + D[(v,w)]
                p.append(w)
    return max(W)

from collections import defaultdict
N = int( input())
E = [ [] for _ in range(N)]
D = defaultdict( int)
for _ in range(N-1):
    a, b, w = map( int, input().split())
    E[a].append(b)
    E[b].append(a)
    D[(a,b)] = D[(b,a)] = w
print( diameter( N, E, D))
