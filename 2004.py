# 2004 - 조합 0의 개수

''' 시간초과 - 팩토리얼 '''
# def fact(n) :
#     answer = 1
#     for i in range(2, n + 1) :
#         answer *= i
#     return answer

# def bino_coef(n, r) :
#     return fact(n) // fact(r) // fact(n - r)

# N, K = map(int, input().split())
# string = list(str(bino_coef(N, K)))
# string.reverse()
# answer = 0
# for i in string :
#     if i != '0' :
#         break
#     answer += 1
# print(answer)

''' 효율적인 방법 ''' 
''' 1676 참고'''
''' 효율적인 방법 '''
'''
n 에서 5로 나누어 떨어지는 수가 몇개인지 구하는 방법
ex) n = 100 인경우 100 / 5 = 20
하지만 여기서 100의 인수인 25는 5를 2개 추가로 가지고 있기 떄문에
더 세줘야한다.
(100 // 25 => 4개)
100!의 0의 개수 = 20 + 4 ==> 24
 '''
N, M = map(int, input().split())
def count_five(n, k) :
    cnt = 0
    while(n != 0) :
        n //= k
        cnt += n
    return cnt

five = count_five(N, 5) - count_five(M, 5) - count_five(N - M, 5)
two = count_five(N, 2) - count_five(M, 2) - count_five(N - M, 2)
print(min(five, two))

