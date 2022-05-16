# 4949 - 균형잡힌 세상 - 스택
while True :
    string = input()
    if string == "." :
        break
    stack = []
    
    for i in string :
        if i == '(' or i == '[' :
            stack.append(i)
        elif i == ']' :
            if len(stack) != 0 and stack[-1] == '[' :
                stack.pop()
            # [] 한쌍 확인, stack을 비워줌
            else :
                stack.append(']')
                break
        elif i == ')' :
            if len(stack) != 0 and stack[-1] == '(' :
                stack.pop()
            else:
                stack.append(')')
                break
    if len(stack) == 0 :
        print("yes")
    else:
        print("no")