# 프로그래머스 - 2021 KAKAO BLIND RECRUITMENT
# 신규 아이디 추천

def solution(new_id):
    answer = ''
    print(new_id)

    # Part 1
    new_id = new_id.lower()
    print("Part 1 :",answer)

    # Part 2
    for i in new_id :
        if i.isalnum() or i in '-_.' :
            answer += i
    print("Part 2 :",answer)
    
    # Part 3
    while '..' in answer :
        answer = answer.replace('..', '.')
    print("Part 3 :",answer)

    # Part 4
    if answer[0] == '.' and len(answer) > 1 :
        answer = answer[1:]
    if answer[-1] == '.' :
        answer = answer[:-1]
    print("Part 4 :",answer)

    # Part 5
    if answer == '' :
        answer = 'a'
    print("Part 5 :",answer)

    # Part 6
    if len(answer) >= 16 :
        answer = answer[:15]
    if answer[-1] == "." :
        answer = answer[:14]
    print("Part 6 :",answer)

    # Part 7
    if len(answer) <= 2 :
        result = 3 - len(answer)
        answer = answer + answer[-1] * result
    print("Part 7 :", answer)

    print("ANSWER : ", answer)
    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))