# 4948 - 베르트랑 공존

''' 시간초과 '''
import math

def prime_number(N) :
    for i in range(2, int(math.sqrt(N) + 1)) :
        if N % i == 0 :
            return False
    return True
while True :
    N = int(input())
    if N == 0 :
        break
    elif N == 1 :
        print(1)
    else :
        result = []
        for i in range(N, 2 * N + 1) :
            if prime_number(i) :
                result.append(i)
        print(len(result))
