# 프로그래머스 - 2021 카카오 채용연계형 인턴십
# 숫자 문자열과 영단어 (100/100)

def solution(s):
    answer = 0
    if "zero" in s :
        s = s.replace("zero", "0")
    if "one" in s :
        s = s.replace("one", "1")
    if "two" in s :
        s = s.replace("two", "2")
    if "three" in  s :
        s = s.replace("three", "3")
    if "four" in s :
        s = s.replace("four", "4")
    if "five" in s :
        s = s.replace("five", "5")
    if "six" in s :
        s = s.replace("six", "6")
    if "seven" in s :
        s = s.replace("seven", "7")
    if "eight" in s :
        s = s.replace("eight", "8")
    if "nine" in s :
        s = s.replace("nine", "9")
    answer = int(s)
    return answer

# 다른 풀이
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution1(s) :
    answer = s
    for key, value in num_dic.items() :
        answer = answer.replace(key, value)
    return int(answer)

print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))

print(solution1("one4seveneight"))
print(solution1("23four5six7"))
print(solution1("2three45sixseven"))
print(solution1("123"))
