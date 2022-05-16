# 7568 - 덩치
N = int(input())
people = []
for i in range(N) :
    temp = list(map(int, input().split()))
    people.append(temp)

for i in people :
    rank = 1
    for j in people :
        if i[0] < j[0] and i[1] < j[1] :
            rank += 1
    print(rank, end = ' ')