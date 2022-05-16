# 숫자 카드

''' 시간 초과 소스 -> 순차탐색 '''
# N = int(input())
# NS = list(map(int, input().split()))
# M = int(input())
# MS = list(map(int, input().split()))

# answer = []
# for i in MS :
#     if i in NS :
#         answer.append(1)
#     else :
#         answer.append(0)
# for i in answer :
#     print(i, end = ' ')

''' 이분 탐색 '''
import sys
N = int(input())
NS = list(map(int, sys.stdin.readline().split()))
M = int(input())
MS = list(map(int, sys.stdin.readline().split()))

NS.sort()
def binary_search(array, target, start, end) :
    while start <= end :
        mid = (start + end) // 2
        if(array[mid] == target) :
            return mid
        elif(array[mid] > target) :
            end = mid - 1
        else :
            start = mid + 1
    return None

for i in range(M) :
    if binary_search(NS, MS[i], 0, N - 1) != None :
        print(1, end = ' ')
    else :
        print(0, end = ' ')
