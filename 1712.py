# 1712 - 손익분기점
# 2021-11-25 AM 12:04 - AM 12:30

temp = input().split()
A = int(temp[0])
B = int(temp[1])
C = int(temp[2])
# i = 1
# while(1) :
#     used_money = A + (B * i)
#     # print(i, used_money)
#     sell_money = C * i
#     # print(i, sell_money)
#     if(used_money < sell_money) :
#         print(i)
#         break
#     if(B >= C) :
#         print(-1)
#         break
#     i += 1

if B >= C :
    print(-1)
else :
    print(int(A/(C-B)+1))

'''
1000 70 170
1대 1070 170
2대 1140 340
3대 1210 510
4대 1280 680
5대 1350 850
6대 1420 1020
7대 1490 1190
8대 1560 1360
9대 1630 1530
10대 1700 1700
11대 1770 1870

3 2 1
5 1
6 2
7 3
8 4

210000000 9 10
'''