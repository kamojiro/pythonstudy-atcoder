def fft(f:list, inverse:int) -> list:
    from math import log2, cos, sin, pi
    deg = len(f)
    if deg == 1:
        return f
    N = int( log2( deg-1))+1
    f += [0]*( pow(2,N) - deg)
    zeta = 1 # 2^N-th root of unity
    before = f
    twopow = 1

    for n in range(1,N+1):
        after = []
        I = pow(2,n)
        J = pow(2,N-n)
        zeta = complex(cos(2*pi/I), inverse*sin(2*pi/I))
        diff = pow(2, N-n)
#        print(I, J)
        for i in range(I):
            bi = i%(I//2)*J*2
            zetai = pow(zeta, i)
            for j in range(J):
                t = before[bi + j] + before[bi + j + J]*zetai
                after.append(t)
        before = after
    return after

def convolution(f,g):
    from math import log2
    n = len(f)
    m = len(g)
    if n == 1 and m == 1:
        return [f[0]*g[0]]
    l = int( log2( n+m-1))+1
    pl = pow(2,l)
    f += [0]*(pl-n)
    g += [0]*(pl-m)
    Ff = fft(f,1)
    Fg = fft(g,1)
    FfFg = [ Ff[i]*Fg[i] for i in range(pl)]
    return list( map(lambda x:int( x.real+0.4), map(lambda x: x/pl, fft(FfFg, -1)[:n+m-1])))

def main():
    f = [1,1]
    g = fft(f, 1)
    print(g)
    print( list( map(lambda x:int(x.real+0.5), map(lambda x:x/2, fft(g,-1) ))))
    f = [1,2]
    g = [3,5]
    print( convolution(f,g))
if __name__ == '__main__':
    main()

