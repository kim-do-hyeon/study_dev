def solution(lottos, win_nums):
    answer = []
    win_count = 0
    lottos = sorted(lottos)
    win_nums = sorted(win_nums)
    print(lottos)
    for i in lottos :
        if i in win_nums :
            win_count += 1
    
    print(win_count)
    compare_list = [x for x in lottos if x not in win_nums]
    print(compare_list)

    return answer

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))