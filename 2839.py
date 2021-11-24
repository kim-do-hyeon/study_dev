# 2839 - 설탕 배달
# 2021-11-24 PM 11:49 - PM 11:58

num = int(input())
result = 0
while(num >= 0) :
    if(num % 5 == 0) :
        result += (num // 5)
        print(result)
        break
    num -= 3
    result += 1
else :
    print(-1)