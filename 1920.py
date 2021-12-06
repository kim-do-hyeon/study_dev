# 1920 - 수찾기
N = int(input())
N_list = list(map(int, input().split()))
N_list.sort()
M = int(input())
M_list = list(map(int, input().split()))

# # for i in M_list :
# #     result = 0
# #     for j in N_list :
# #         if(i == j) :
# #             result = 1
# #     print(result)

# set_list = N_list & M_list
# for i in M_list :
#     result = 0
#     for j in set_list :
#         if (i == j) :
#             result = 1
#     print(result)
for i in M_list :
    left, right = 0, len(N_list) - 1
    find = False
    while True :
        median = (left + right) // 2
        if i == N_list[median] :
            print(1)
            find = True
            break
        elif i > N_list[median] :
            left = median + 1
        elif i < N_list[median] :
            right = median - 1
        
        if left > right :
            break
    if not find :
        print(0)