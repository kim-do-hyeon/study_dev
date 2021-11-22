# 2292 - 벌집
# 2021-11-23 AM 2:06 - AM 2:12

# n = int(input())
# count = 1
# bee_house_length = 6
# cnt = 1

# while n > cnt :
#     count += 1
#     cnt += bee_house_length
#     bee_house_length += 6
# print(count)

# Solution
'''
지나가야하는 방의 개수 1개 : 1
지나가야하는 방의 개수 2개 : 2,3,4,5,6,7
지나가야하는 방의 개수 3개 : 8,9,10,11,12,13,14,15,16,17,18,19
지나가야하는 방의 개수 4개 : 20 ~ 37
지나가야하는 방의 개수 5개 : 38 ~ 61

방을 1개 거쳐야 하는 숫자는 6개
방을 2개 거쳐야 하는 숫자는 12개
방을 3개 거쳐야 하는 숫자는 18개
...

이렇게 6씩 증가한다.

'''

n = int(input())
cnt = 1
count = 1
bee_house = 6
while n > cnt :
    count += 1
    cnt += bee_house
    bee_house += 6
print(count)