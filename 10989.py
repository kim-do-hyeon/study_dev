# 10989 - 수 정렬하기 3
'''
N = int(input())
temp_list = []
for i in range(N) :
    temp_list.append(int(input()))
temp_list.sort()
for i in temp_list :
    print(i)
'''

# Time : append <<<<<< readline

import sys
N = int(input())

dic = {}

for i in range(N):
    a = int(sys.stdin.readline())

    if a in dic:
        dic[a] =  dic[a] +1

    else:
        dic[a] = 1

for sorted in sorted(dic.items()):
    for i in range(sorted[1]):
        print(sorted[0])