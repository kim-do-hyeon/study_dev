# 1158 - 요세푸스 문제
N, K = map(int, input().split())
array = [i for i in range(1, N + 1)]
answer = []
index = 0 
for i in range(N) :
    index += K - 1
    if index >= len(array) :
        index = index % len(array)
    answer.append(str(array.pop(index)))
print("<",", ".join(answer), ">", sep = '')

'''
N명의 사람들이 있을때, K값을 주기로 삼아 사람들을 제거한다.
K 값이 사람들의 인원수를 초과하면(8번 라인)
사람의 이원수로 나눈 나머지로 값을 초기화 한다.
'''