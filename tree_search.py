from collections import deque

#深さ優先探索
def depth_first_search(T):
    D = deque()
    if len(T) > 0:
        D.append(T) #;show(D)
    while len(D) > 0:
        L,a,R = D.pop()
        print(a,end = ',') #;show(D)
        if len(L) > 0:
            D.append(L) #;show(D)
        if len(R) > 0:
            D.append(R) #;show(D)
    print()

#幅優先探索
def breads_first_search(T):
    D = deque()
    if len(T) > 0:
        D.append(T) #;show(D)
    while len(D) > 0:
        L,a,R = D.popleft()
        print(a,end = ',')
        if len(L) > 0:
            D.append(L)
        if len(R) > 0:
            D.append(R)
    print()
