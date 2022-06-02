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


# ''' 시간초과 2 '''
# from math import sqrt
# while True :
#     n = int(input())
#     if n == 0 :
#         break
#     count = 0

#     for i in range(n + 1, 2 * n + 1) :
#         if  i == 1 :
#             continue
#         elif i == 2 :
#             count += 1
#             continue
#         else :
#             for j in range(2, int(sqrt(i) + 1)) :
#                 if i % j == 0 :
#                     break
#             else :
#                 count += 1
#     print(count)

# 10 ~ 20
# 11 13 17 19
# 13  ~ 26
# 17 19 23

def sosu(n):
    if n ==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True							#소수 구하는 방식은 위와 같다

all_list = list(range(2,246912))		#문제에서 제한한 범위
memo = []								#for문 밖에 리스트 정의

for i in all_list:						#2부터 2*123,456 범위
    if sosu(i):							#sosu함수에 해당하면
        memo.append(i)					#리스트에 추가

n = int(input())

while True:
    count=0					#갯수를 세야하는 조건 때문에 카운트
    if n == 0 :
            break
    for i in memo:			#memo리스트 중에서
        if n < i <=2*n:		#입력한 값의 범위 내에서 값이 있으면
            count+=1		#있을 때 마다 카운트 +1
    print(count)
    n = int(input())		#0 입력받기 전까지 계속 해야하므로 입력 받음