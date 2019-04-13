def sort(A):
    construct_heap(A, 0);print(A)
    for last in range(len(A) - 1, 0, -1):
        A[0], A[last] = A[last], A[0];print(A)
        exchange_nodes(A,0,last - 1); print(A)

def left(n):
    return 2 * n +1

def right(n):
    return 2*n +2

def exchange_nodes(A,n,last):
    if last < left(n):
        return
    child = left(n)
    if right(n) <= last:
        if A[left(n)] < A[right(n)]:
            child = right(n)
    if A[n] < A[child]:
        A[n], A[child] = A[child], A[n]
        exchange_nodes(A,child,last)

def construct_heap(A,n):
    last = len(A) - 1
    if last < left(n):
        return
    construct_heap(A,left(n))
    if right(n) <= last:
        construct_heap(A, right(n))
    exchange_nodes(A,n,last)
