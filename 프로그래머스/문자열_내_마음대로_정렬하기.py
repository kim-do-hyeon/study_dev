# 프로그래머스 - 연습문제
# 문자열 내 마음대로 정렬하기

def solution(strings, n):
    answer = []
    
    ''' CASE 1'''
    # for i in range(len(strings)) :
    #     strings[i] = [strings[i], strings[i][n]]
    # temp = (sorted(strings, key = lambda a : a[1]))
    # for i in temp :
    #     answer.append(i[0])
    # print(answer)
    # return answer

    ''' CASE 2'''
    # temp = []
    # for i in strings :
    #     temp.append(i[n])
    # temp.sort()

    # for i in temp :
    #     for j in strings :
    #         if j[n] == i :
    #             answer.append(j)

    # return answer

    ''' CASE 3 '''
    return sorted(sorted(strings), key=lambda x: x[n])

print(solution(["sun", "bed", "car"],1))
print(solution(["abce", "abcd", "cdx"],2))