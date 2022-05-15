# 15652 - N과 M (4) - 백트래킹

N, M = list(map(int, input().split()))

Array = []

def DFS(s) :
    if len(Array) == M :
        print(' '.join(map(str, Array)))
        return
    for i in range(s, N + 1) :
            Array.append(i)
            DFS(i)
            Array.pop()
DFS(1)