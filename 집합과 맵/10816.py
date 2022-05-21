# 10816 - 숫자카드

''' 시간초과 '''
# N = int(input())
# N_list = list(map(int, input().split()))
# M = int(input())
# M_list = list(map(int, input().split()))
# for i in M_list :
#     count = 0
#     for j in N_list :
#         if i == j :
#             count += 1
#     print(count, end = ' ')
import sys
N = int(input())
N_list = list(map(int, input().split()))
N_dict = {}
for i in N_list :
    try :
        N_dict[i] += 1
    except :
        N_dict[i] = 1
M = int(input())
M_list = list(map(int, input().split()))
for i in M_list :
    try :
        print(N_dict[i], end = ' ')
    except :
        print(0, end = ' ')