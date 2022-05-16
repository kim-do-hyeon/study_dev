# 2609 - 최대공약수와 최소공배수

# 유클리드 호제법
X, Y = map(int, input().split())

def gcd(X, Y) :
    while(Y != 0) :
        R = X % Y
        X = Y
        Y = R
    return X

def lcm(X, Y) :
    return int((X * Y) / gcd(X, Y))

print(gcd(X, Y))
print(lcm(X, Y))