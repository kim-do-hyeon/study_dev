# 15650 - N과 M (2) - 백트래킹

N, M = list(map(int, input().split()))

Array = []

def DFS(s) :
    if len(Array) == M :
        print(' '.join(map(str, Array)))
        return

    for i in range(s, N + 1) :
        if i not in Array :
            Array.append(i)
            DFS(i + 1)
            Array.pop()
DFS(1)