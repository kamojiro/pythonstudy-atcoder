def Ack(m,n):
    if m == 0:
        return n+1
    elif n == 0:
        return Ack(m-1,1)
    else:
        return Ack(m-1, Ack(m,n-1))
m, n = map( int, input().split())
print(Ack(m,n))
