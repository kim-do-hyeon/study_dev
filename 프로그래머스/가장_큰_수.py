def solution(numbers):
    # print(numbers)
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x:x * 3, reverse=True)
    # print(numbers)
    answer = str(int(''.join(numbers)))
    # print(answer)
    return answer
    


solution([6, 10, 2])
solution([3, 30, 34, 5, 9])