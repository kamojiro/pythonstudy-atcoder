def shortest_length(G, start):
    S = {start:0}; D = {}
    while len(S) > 0:
        x = select_min(S); m = S[x]; del S[x]; D[x] = m
        for (y, w) in edge(G,x):
            if y in S:
                if S[y] > m + w:
                    S[y] = m + w
            elif y not in D:
                S[y] = m + w
        print('仮',S,'確定',D)

def select_min(S):
    m = -1
    for a in S:
        if m == -1 or m > S[a]:
            x = a
            m = S[a]
    return x

def edge(G,x):
    return ([(b,G[(a,b)]) for (a,b) in G if a == x]
                + [(a,G[(a,b)]) for (a,b) in G if b == x])
                
