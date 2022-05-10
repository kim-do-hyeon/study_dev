# 소인수 분해

N = int(input())
answer = []
value = 2
if N == 1:
    quit()
while value <= N :
    if N % value == 0 :
        answer.append(value)
        N /= value
    else :
        value += 1
for i in answer :
    print(i)