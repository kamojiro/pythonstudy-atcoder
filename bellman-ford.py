#http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_B&lang=jp

import sys
input = sys.stdin.readline
from collections import deque
def main():
    N, M, r = map( int, input().split())
    d = dict()
    E = [[] for _ in range(N)]
    for _ in range(M):
        a, b, c = map( int, input().split())
        d[(a,b)] = c
        E[a].append(b)
    INF = 10**14*2
    V = [INF]*N
    V[r] = 0
    for _ in range(N-1):
        for e in d:
            s, t = e
            if V[s] + d[e] < V[t]:
                V[t] = V[s] + d[e]
    q = deque([r])
    W = [False]*N
    while q:
        v = q.pop()
        for w in E[v]:
            if W[w] == False:
                W[w] = True
                q.append(w)
    for e in d:
        s, t = e
        if V[s] + d[e] < V[t] and (W[s] == True or W[t] == True):
            print("NEGATIVE CYCLE")
            return
    for i in range(N):
        if V[i] >= 10**14:
            print("INF")
            continue
        print(V[i])
    # #if you want to know whether its path has negative cycle, we need followings.
    # E = [ V[i] for i in range(N)]
    # for _ in range(N-1):#probably OK, maybe N
    #     for e in d:
    #         s, t = e
    #         if E[s] + d[e] < E[t]:
    #             E[t] = E[s] + d[e]
    # #if you want to know whether its path has negative cycle, we need followings.
    # for i in range(N):
    #     if V[i] == E[i]:
    #         print(V[i])
    #     else:
    #         print("NEGATIVE CYCLE")
        
if __name__ == '__main__':
    main()
