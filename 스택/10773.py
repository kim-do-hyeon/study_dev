# 10773 - 제로 - 스택


'''
단순 스택에서의 pop 문제이다.
'''
K = int(input())
stack = []
for i in range(K) :
    temp = int(input())
    if temp == 0 :
        stack.pop()
    else :
        stack.append(temp)
print(sum(stack))