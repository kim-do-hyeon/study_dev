def solution(n):
    answer = 0
    temp = []
    for i in range(1, n) :
        if n % i == 1 :
            temp.append(i)
    answer = min(temp)
    return answer

print(solution(10))
print(solution(12))