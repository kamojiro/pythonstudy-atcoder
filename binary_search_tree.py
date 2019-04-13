def show(T):
    if len(T) == 0:
        return ''
    L, data, R = T
    return '(' + show(L) + str(data) + show(R) + ')'

def insert(T,n):
    if len(T) == 0:
        return ((),n,())
    L, data, R = T
    if n == data:
        return T
    if n < data:
        return (insert(L,n),data,R)
    return (L,data,insert(R,n))

def search(T,n):
    if len(T) == 0:
        return False
    L,data,R = T
    if n == data:
        return True
    if n < data:
        return search(L,n)
    return search(R,n)
    
def remove(T,n):
    if len(T) == 0:
        return()
    L,data,R = T
    if n == data:
        if len(L) == 0:
            return(R)
        if len(R) == 0:
            return(L)
        m, X = remove_min(R)
        return (L,m,X)
    if n < data:
        return (remove(L,n),data,R)
    return (L,data,remove(R,n))

def remove_min(T):
    L,data,R = T
    if len(L) == 0:
        return(data,R)
    m,X = remove_min(L)
    return (m, (X, data, R))
            
