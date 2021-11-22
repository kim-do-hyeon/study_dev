# 2775 - 부녀회장이 될테야
# 2021-11-23 AM 1:10 - AM 1:21

num_input = int(input())
for i in range(num_input) :
    floor = int(input())
    num = int(input())
    floor_0_list = [x for x in range(1, num + 1)]
    for j in range(floor) :
        for k in range(1, num) :
            floor_0_list[k] += floor_0_list[k - 1]
    print(floor_0_list[-1])


# Solution
'''
예를 들어서 3층 3호에 살고자 한다.
3층 3호에 살려고 한다면 2층 1호, 2층 2호, 2층 3호에 사는
사람들의 합만큰 3층 3호에 데리고 살아햐한다.

그럼 3층 2호를 산다고 가정하면, 2층 1호, 2층 2호에 사는 사람들의
합만큼 데리고 살아야한다.

그렇다면 3층 3호에 데리고 살아야 하는 인원은 3층 2호에 데리고 살아햐 하는
인원 + 2층 3호에 데리고 살아햐 하는 인원이 된다.

입력 예제인 2 1 3 2 3 을 기준으로
1층 3호에 산다면, 0층 1호, 0층 2호, 0층 3호에 있는
각각 1명, 2명 3명을 데리고 와서 6명이 되어야 한다.

2층 3호에 산다고 가정하면, 1층 1호, 1층 2호, 1층 3호에 있는 사람들을
데리고 살아햐 한다.
1층 3호에는 6명이 살고 있고, 1층 2호에는 3명, 1층 1호에는 1명,
그래서 2층 3호에는 10명이 살아야한다.
'''

# num = int(input())
# for i in range(num) :
#     result = 0
#     floor = int(input())
#     ho = int(input())
#     list_ = [x for x in range(1, ho + 1)]
#     for j in range(floor) :
#         for k in range(1, ho) :
#             list_[k] += list_[k - 1]
#     print(list_[-1])