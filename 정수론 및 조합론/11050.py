# 11050 - 이항 계수 1

def fact(n) :
    answer = 1
    for i in range(2, n + 1) :
        answer *= i
    return answer

def bino_coef(n, r) :
    return fact(n) // fact(r) // fact(n - r)


N, K = map(int, input().split())
print(bino_coef(N, K))