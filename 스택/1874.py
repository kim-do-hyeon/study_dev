# 1874 - 스택 수열 - 스택
n = int(input())
count = 0
stack = []

answer = []

for i in range(0, n) :
    x = int(input())
    while count < x :
        count += 1
        stack.append(count)
        answer.append("+")
    
    if stack[-1] == x :
        stack.pop()
        answer.append("-")
    else :
        print("NO")
        quit()
for i in answer :
    print(i)
