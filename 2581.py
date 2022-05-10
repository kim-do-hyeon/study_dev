# 소수

M = int(input())
N = int(input())
answer = []

for i in range(M, N + 1) :
    err = 0
    if i > 1 :
        for j in range(2, i) :
            if i % j == 0:
                err += 1
                break
        if err == 0 :
            answer.append(i)

if len(answer) > 0 :
    print(sum(answer))
    print(min(answer))
else :
    print(-1)