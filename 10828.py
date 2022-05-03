import sys

input=sys.stdin.readline
stack = []
def push(x) :
    stack.append(x)

def pop() :
    if len(stack) > 0 :
        temp = stack[-1]
        stack.pop()
        print(temp)
        # return temp
    else :
        # return -1
        print(-1)

def size() :
    # return len(stack)
    print(len(stack))

def empty() :
    if len(stack) != 0 :
        print(0)
        # return 0
    else :
        # return 1
        print(1)

def top() :
    if len(stack) != 0 :
        print(stack[-1])
    else :
        print(-1)


n = int(input())
for i in range(n) :
    command = input().split()
    if command[0] == "push" :
        push(int(command[1]))
    elif command[0] == "top" :
        top()
    elif command[0] == "size" :
        size()
    elif command[0] == "empty" :
        empty()
    elif command[0] == "pop" :
        pop()
