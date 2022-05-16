# 서로 다른 부분 문자열의 개수
s = input()
answer = []
for i in range(len(s)) :
    for j in range(i, len(s)) :
        temp = (s[i:j + 1])
        answer.append(temp)
print(len(set(answer)))