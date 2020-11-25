# # 음계

# list = list(map(int, input().split()))

# ascending = False
# descending = False

# for index in range(len(list)-1):
#     if list[index] < list[index+1]:
#         ascending = True
#     else:
#         descending = True

#     if ascending == True and descending == True:
#         print("mixed")
#         break

# if ascending == True and descending == False:
#     print("ascending")
# elif ascending == False and descending == True:
#     print("descending")

# 블랙잭

n, m = map(int, input().split())
list = list(map(int, input().split()))

result = 0
length = len(list)

for i in range(0, length):
    for j in range(i+1, length):
        for k in range(j+1, length):
            sum = list[i] + list[j] + list[k]
            if sum < m:
                result = max(result, sum)

print(result)