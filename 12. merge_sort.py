# 병합정렬

# split 함수 구현

def mergesplit(data):
    if len(data) <= 1:
        return data

    medium = int(len(data)/2)
    left = mergesplit(data[:medium])
    right = mergesplit(data[medium:])

    return merge(left, right)

