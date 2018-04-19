# 冒泡排序法
# 每次冒泡完成后，下一次冒泡的list的长度比之前少1
# 所以list的长度是动态的
def bubble_sort(arr):
    for n in range(len(arr)-1, 0, -1):
        for i in range(n):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

# 测试
la = [41, 2, 88, 16, 566, 258]
print(bubble_sort(la))