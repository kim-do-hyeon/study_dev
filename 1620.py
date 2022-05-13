# 1620 - 나는야 포켓몬 마스터 이다솜

''' 시간초과 '''
'''
N, M = map(int, input().split())
poketmon = []
for i in range(N) :
    temp = input()
    poketmon.append(temp)

question = []
for i in range(M) :
    temp = input()
    question.append(temp)

for i in question :
    try :
        i = int(i) - 1
        print(poketmon[i])
    except :
        print(poketmon.index(i) + 1)
'''

''' 시간 초과 2 '''
'''
import sys
N, M = map(int, input().split())
poketmon = []
for i in range(N) :
    temp = sys.stdin.readline().strip()
    poketmon.append(temp)

question = []
for i in range(M) :
    temp = sys.stdin.readline().strip()
    question.append(temp)

for i in question :
    try :
        i = int(i) - 1
        print(poketmon[i])
    except :
        print(poketmon.index(i) + 1)
'''

''' DICT 사용 '''
import sys
N, M = map(int, input().split())
poketmon = []
poketmon_dict = {}

for i in range(N) :
    temp = sys.stdin.readline().strip()
    poketmon.append(temp)
    poketmon_dict[temp] = i + 1

for i in range(M) :
    temp = sys.stdin.readline().strip()

    if temp.isdigit() :
        print(poketmon[int(temp) - 1])
    else :
        print(poketmon_dict[temp])
