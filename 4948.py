# 4948 - 베르트랑 공존

''' 시간초과 '''
# import math

# def prime_number(N) :
#     for i in range(2, int(math.sqrt(N) + 1)) :
#         if N % i == 0 :
#             return False
#     return True
# while True :
#     N = int(input())
#     if N == 0 :
#         break
#     elif N == 1 :
#         print(1)
#     else :
#         result = []
#         for i in range(N, 2 * N + 1) :
#             if prime_number(i) :
#                 result.append(i)
#         print(len(result))


# 에라토스체 사용
# n = int(input())
# a = [False, False] + [True] * (2 * n - 1)
# primes = []

# for i in range(n, (2 * n) + 1) :
#     if a[i] :
#         primes.append(i)
#         for j in range(2 * i, (2 * n) + 1, i) :
#             a[j] = False
# print(primes)
# print(len(primes))


''' 시간초과 2 '''
from math import sqrt
while True :
    n = int(input())
    if n == 0 :
        break
    count = 0

    for i in range(n + 1, 2 * n + 1) :
        if  i == 1 :
            continue
        elif i == 2 :
            count += 1
            continue
        else :
            for j in range(2, int(sqrt(i) + 1)) :
                if i % j == 0 :
                    break
            else :
                count += 1
    print(count)

# 10 ~ 20
# 11 13 17 19
# 13  ~ 26
# 17 19 23