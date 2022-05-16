# 소수 찾기
n = int(input())
list_ = map(int, input().split())
answer = 0
def is_prime(x) :
    global answer
    for i in range(2, x) :
        if x % i == 0 :
            return False
    answer += 1
for i in list_ :
    if i == 1 :
        pass
    else :
        is_prime(i)
print(answer)