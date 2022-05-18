# 4153 - 직각삼각형
while True :
    list_ = list(map(int, input().split()))
    if sum(list_) == 0 :
        break
    MAX_VALUE = max(list_)
    list_.remove(MAX_VALUE)
    if MAX_VALUE * MAX_VALUE == list_[0] * list_[0] + list_[1] * list_[1] :
        print("right")
    else :
        print("wrong")
