# 18870 - 좌표 압축

import sys

input = sys.stdin.readline
N = int(input())

position = list(map(int, input().split()))
position_check = sorted(list(set(position)))

dic = {}
for i in range(len(position_check)) :
    dic[position_check[i]] = i

for i in position :
    print(dic[i], end = ' ')

'''
새 리스트에 set 함수를 통해서 입력받은 좌표의 값을 중복 제거후 정렬한다.
dict을 통해서 해당 좌표의 값들의 인덱스를 저장후
다시 기존 좌표의 리스트를 돌면서, 인덱스를 출력한다.
'''