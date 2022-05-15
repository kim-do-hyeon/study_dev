# 1010 - 다리 놓기

''' 조합을 통해 푸는 문제 '''
''' nCr '''
''' n! / (n - r)! * n!'''

def fact(n) :
    value = 1
    for i in range(1, n + 1) :
        value *= i
    return value

T = int(input())
for i in range(T) :
    X, Y = map(int, input().split())
    print(fact(Y) // (fact(X) * (fact(Y - X))))