# 1339 - 단어 수학
N = int(input())
dic = {}
word_list = []
for _ in range(N) :
    word_list.append(input())

for word in word_list :
    root = len(word) - 1
    for i in word :
        if i in dic :
            dic[i] += pow(10, root)
        else :
            dic[i] = pow(10, root)
        root -= 1

dic = sorted(dic.values(), reverse=True)
result, m = 0, 9
for value in dic :
    result += value * m
    m -= 1
print(result)