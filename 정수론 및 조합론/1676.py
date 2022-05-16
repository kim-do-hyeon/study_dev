# 1076 - 팩토리얼 0의 개수

def fact(n) :
    answer = 1
    for i in range(2, n + 1) :
        answer *= i
    return answer

N = int(input())
string = list(str(fact(N)))
string.reverse()

result = 0
for i in string :
    if i != '0' :
        break
    result += 1
print(result)

''' 효율적인 방법 '''
'''
n 에서 5로 나누어 떨어지는 수가 몇개인지 구하는 방법
ex) n = 100 인경우 100 / 5 = 20
하지만 여기서 100의 인수인 25는 5를 2개 추가로 가지고 있기 떄문에
더 세줘야한다.
(100 // 25 => 4개)
100!의 0의 개수 = 20 + 4 ==> 24
 '''
# N = int(input())
# cnt = 0
# while(N != 0) :
#     N //= 5
#     cnt += N
# print(cnt)

