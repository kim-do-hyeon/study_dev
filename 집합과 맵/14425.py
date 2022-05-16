#  문자열 집합
N, M = map(int, input().split())

S = []
for i in range(N) :
    temp = input()
    S.append(temp)

check_list = []
for i in range(M) :
    temp = input()
    check_list.append(temp)
count = 0
for i in check_list :
    if i in S :
        count += 1

print(count)

