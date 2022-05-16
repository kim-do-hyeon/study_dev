# 소수 구하기 - 에라토스테네스의 체
M, N = map(int, input().split())

def prime(n) :
    if n == 1 :
        return False
    else :
        for i in range(2, int(n ** 0.5) + 1) :
            if n % i == 0 : 
                return False
        return True

for i in range(M, N + 1) :
    if prime(i) :
        print(i)