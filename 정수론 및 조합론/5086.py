# 5086 - 배수와 약수
while True :
    x, y = map(int, input().split())
    if x == 0 and y == 0 :
        break
    if x % y == 0 :
        print("multiple")
    elif y % x == 0 :
        print("factor")
    else :
        print("neither")