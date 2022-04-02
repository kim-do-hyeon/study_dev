# 프로그래머스 - 2022 KAKAO BLIND CODING TEST
# 신고 결과 받기
# 75 / 100

def solution(id_list, report, k):
    report = set(report)
    report = list(report)

    reported_user = []
    for i in report :
        temp = i.split()
        reported_user.append(temp[1])

    dic = dict()
    for i in reported_user :
        try :  dic[i] = dic[i] + 1
        except : dic[i] = 1

    banned = []
    for key, value in dic.items() :
        if value >= k :
            banned.append(key)

    return_user = {}
    for i in range(len(id_list)) :
        count = 0
        for j in report :
            temp = j.split()
            if(id_list[i] == temp[0] and temp[1] in banned) :
                count += 1
        return_user[i] = count
    answer = list(return_user.values())
    return (answer)
            

solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)
print("===================")
solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"],3)