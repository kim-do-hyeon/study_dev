# 1316 - 그룹 단어 체커
# 2021-11-23 AM 1:32 - AM 2:00

# num = int(input())
# value = 0
# for i in range(num) :
#     temp = input()
#     result = 0
#     for idx in range(len(temp) - 1):
#         if temp[idx] != temp[idx + 1] :
#             new_temp = temp[idx + 1:]
#             if new_temp.count(temp[idx]) > 0 :
#                 print("COUNT!", new_temp.count(temp[idx]))
#                 result += 1
#     if result == 0 :
#         value += 1
# print(value)


num = int(input())
result = 0
for i in range(num):
    word = input()
    value = 0
    for idx in range(len(word) - 1) :
        if word[idx] != word[idx + 1] :
            new_word = word[idx + 1 : ]
            if new_word.count(word[idx]) > 0 :
                value += 1
    if value == 0 :
        result += 1
print(result)

