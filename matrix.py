def product3(A,B):
    C = [[0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                C[i][j] += A[i][k]*B[k][j]
    return C

def product(A,B,N):
    C = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i][j] += A[i][k]*B[k][j]
    return C

#import sys
#input = sys.stdin.readline
def main():
    A = [[1,0,0],[0,2,0],[0,0,3]]
    B = [[1,2,3],[4,5,6],[7,8,9]]
    print(product3(A,B))
    N = 3
    print(product(A,B,3))
if __name__ == '__main__':
    main()

