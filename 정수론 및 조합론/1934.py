# 1934 - 최소공배수

def GCD(X, Y) :
    while(Y != 0) :
        R = X % Y
        X = Y
        Y = R
    return X

def LCM(X, Y) :
    return int((X * Y) / GCD(X, Y))


T = int(input())

for i in range(T) :
    X, Y = map(int, input().split())
    print(LCM(X, Y))