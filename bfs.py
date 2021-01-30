
def bfs01(N, E, s, INF=10**10):
    from collections import deque    
    # N: vertex
    # E[i] = [vetices connected to i]
    # s: start
    V = [INF]*N
    d = deque([s])
    V[s] = 0
    while d:
        v = d.popleft()
        now = V[v]
        for w in E[v]:
            if V[w] < INF:
                continue
            V[w] = now+1
            d.append(w)
    # print(V)
    return V

def bfs02(N, E, s, g, INF=10**10):
    from collections import deque
    # N: vertex
    # E[i] = [vetices connected to i]
    # s: start
    # g: goal
    INF = 10**10
    V = [INF]*N
    d = deque([s])
    V[s] = 0
    while d:
        v = d.popleft()
        now = V[v]
        for w in E[v]:
            if V[w] < INF:
                continue
            if w == g:
                return now+1
            V[w] = now+1
            d.append(w)
    # print(V)
    return V
