def solution(numbers):
    num = list(range(0,10))
    answer = 0
    for i in numbers :
        if i in num :
            answer += i
    return 45 - answer

def solution1(numbers):
    return 45 - sum(numbers)


print(solution([1,2,3,4,6,7,8,0]))