# 음계

list = list(map(int, input().split()))

ascending = False
descending = False

for index in range(len(list)-1):
    if list[index] < list[index+1]:
        ascending = True
    else:
        descending = True

    if ascending == True and descending == True:
        print("mixed")
        break

if ascending == True and descending == False:
    print("ascending")
elif ascending == False and descending == True:
    print("descending")

