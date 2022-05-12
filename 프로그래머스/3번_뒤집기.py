def solution(n):
    answer = 0
    strings = []
    for i in range(1, 100) :
        if(3 ** i) < n :
            temp = (n // (3 ** (i - 1)))
            temp_ = temp % 3
            strings.append(temp_)
            if temp < 9 :
                strings.append(temp // (3))
    print(strings)

    i = 1
    for j in strings :
        num = ((3 ** (len(strings) - i) * j))
        i += 1
        answer += num
    print(answer)
    return answer

print(solution(45))
