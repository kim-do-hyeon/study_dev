# 11650 - 좌표 정렬하기
N = int(input())
position = []
for i in range(N) :
    temp = list(map(int, input().split()))
    position.append(temp)
# print(position)
position = sorted(position, key = lambda x : (x[0], x[1]))
# print(position)
for i in position :
    print(i[0], i[1])