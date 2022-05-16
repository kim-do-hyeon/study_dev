# 9012 - 괄호 - 스택

T = int(input())
for i in range(T) :
    check = input()
    temp = list(check)
    # print(temp)
    count = 0
    for j in temp :
        if j == '(' :
            count += 1
        elif j == ')' :
            count -= 1
        if count < 0 :
            print("NO")
            break
    if count > 0 :
        print("NO")
    elif count == 0 :
        print("YES")