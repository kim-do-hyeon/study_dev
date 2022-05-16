# 3036 - 링

def GCD(X, Y) :
    while(Y != 0) :
        R = X % Y
        X = Y
        Y = R
    return X

N = int(input())
ring = list(map(int, input().split()))
for i in range(1, len(ring)) :
    value = GCD(ring[0], ring[i])
    print("%d/%d" % (ring[0] // value, ring[i] // value))
