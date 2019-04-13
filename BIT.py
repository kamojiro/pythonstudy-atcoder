#N個の変数v_1, ..., v_n
#Q個のクエリ
#各クエリはv_aにwを加えるという操作
#answerは各クエリに対してv_1 + ... + v_aを求める
#クエリごとにどんどんv_1, ..., v_nは更新される
#x-1となっているのは、リストが0番目からになっているから。
#x&(-x)で2進数で表した場合の最も下位にある1の位置を取り出すことができる。
#例えば，10 = 1010なら10を返し、7 = 111なら1を返す。
N, Q = map( int, input().split())
V = list( map( int, input().split()))
def add(A,a,w):#リストに値を追加する関数
    x = a
    while x <= N:
        A[x-1] += w
        x += x&(-x)

def sums(A,a):#k番目までの和
    x = a
    S = 0
    while x != 0:
        S += A[x-1]
        x -= x&(-x)
    return S

A = [0]*N
for i in range(1,N+1):
    add(A,i,V[i-1])
#for i in range(1,N+1): #確認用
#    print(search(A,i))
for _ in range(Q):
    v, w = map( int, input().split())
    add(A,v,w)
    print(sums(A,v))
    
