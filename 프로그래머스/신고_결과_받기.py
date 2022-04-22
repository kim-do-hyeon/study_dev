# 프로그래머스 - 2022 KAKAO BLIND CODING TEST
# 신고 결과 받기

def solution(id_list, report, k):

    # ====== 수정전 ======
    # report = set(report)
    # report = list(report)
    # 불필요하게 list와 set을 따로 쓸 필요 없이, 같이 쓸수 있음.

    # ====== 수정후 ======
    report = list(set(report))
    # ====================================================

    # ====== 수정전 ======
    # reported_user = []
    # for i in report :
    #     temp = i.split()
    #     reported_user.append(temp[1])
    # dic = dict()
    # for i in reported_user :
    #     try :  dic[i] = dic[i] + 1
    #     except : dic[i] = 1
    # 이거도 불필요하게 dic for문과 for문을 따로 쓸 필요 없이, 같이 쓸수 있음.
    # ====== 수정후 ======
    test = []

    dic = dict()
    for i in report :
        temp = i.split()
        test.append([temp[0], temp[1]])
        try :  dic[temp[1]] = dic[temp[1]] + 1
        except : dic[temp[1]] = 1
    # ====================================================



    banned = []
    for key, value in dic.items() :
        if value >= k :
            banned.append(key)

    # ====== 수정전 ======
    # return_user = {}
    # for i in range(len(id_list)) :
    #     count = 0
    #     for j in report :
    #         temp = j.split()
    #         print(temp)
    #         if(id_list[i] == temp[0] and temp[1] in banned) :
    #             count += 1
    #     return_user[i] = count
    # answer = list(return_user.values())
    # print(answer)
    # return (answer)
    #
    # for문을 두번 사용해 시간 초과가 발생

    # ====== 수정후 ======
    return_user = dict.fromkeys(id_list, 0)
    for i in test :
        if(i[0] in return_user and i[1] in banned) :
            return_user[i[0]] += 1
    answer = list(return_user.values())
    print(answer)
    return (answer)
        
            

solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)
print("===================")
solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"],3)