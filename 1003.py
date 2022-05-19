# 1003 - 피보나치 함수

''' 시간 초과 '''
# import sys
# input = sys.stdin.readline
# def fibo(n) :
#     global count_zero, count_one
#     if(n == 0) :
#         count_zero += 1
#         return 0
#     elif(n == 1) :
#         count_one += 1
#         return 1
#     else :
#         return fibo(n - 1) + fibo(n - 2)



# T = int(input())
# for i in range(T) :
#     num = int(input())
#     count_zero = 0
#     count_one = 0
#     fibo(num)
#     print(count_zero, count_one)

''' 성공 '''
T = int(input())
for i in range(T) :
    num = int(input())
    count_zero = [1, 0]
    count_one = [0, 1]
    for j in range(2, num + 1) :
        count_zero.append(count_zero[j - 1] + count_zero[j - 2])
        count_one.append(count_one[j - 1] + count_one[j - 2])
    print(count_zero[num], count_one[num])