# 프로그래머스 - 월간 코드 챌린지 시즌2
# 음양 더하기
def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)) :
        if signs[i] == True : 
            answer += absolutes[i]
        else :
            answer -= absolutes[i]
    print(answer)
    return answer

solution([4,7,12], [True,False,True])