# 11651 - 좌표정렬하기 2

''' 시간 초과 '''
'''
N = int(input())
position = []
for i in range(N) :
    temp = list(map(int, input().split()))
    position.append(temp)
# print(position)
position = sorted(position, key = lambda x : (x[1], x[0]))
# print(position)
for i in position :
    print(i[0], i[1])
'''
''' 시간 초과 2 '''
'''
N = int(input())
position = []
for i in range(N) :
    x, y = (map(int, input().split()))
    position.append([y, x])

position.sort()
for y, x in position :
    print(x, y)
'''

''' sys.stdin.readline 사용 '''
import sys
input = sys.stdin.readline
N = int(input())
position = []
for i in range(N) :
    temp = list(map(int, input().split()))
    position.append(temp)
# print(position)
position = sorted(position, key = lambda x : (x[1], x[0]))
# print(position)
for i in position :
    print(i[0], i[1])

# input을 쓰지말고, sys.stdin.readline 을 쓰자...