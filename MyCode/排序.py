1;冒泡排序
def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

2;选择排序
def selectionSort(arr):
    for i in range(len(arr) - 1):
        # 记录未排序序列中最小数的索引
        min_i = i 
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                nin_i = j
        # 如果找到最小数，将i位置上元素与最小数位置上元素进行交换
        if i != min_i:
            arr[i], arr[min_i] = arr[min_i], arr[i] 

    return arr 

3;插入排序
def insertionSort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i 
        while j > 0 and arr[j-1] > temp:
            arr[j] = arr[j-1] # 原来位置的数往后移动
            j -= 1
        arr[j] = tmp 
    return arr


4;快排
import random 
def partition(arr, low, high):
    x = arr[high]
    i = low - 1  #注意这里
    for j in range(low, high):
        if arr[j] <= arr[high]:  #小于随机选取的值，则依次放在arr左边
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]  # 复原
    return i+1 

def  randomPartition(arr, low, high):
    i = random.randint(low, high)
    arr[i], arr[high] = arr[high], arr[i]  #随机选取值，固定在最后位置
    return partition(arr, low, high)  #获取排序好位置的索引

def quickSort(arr, low, high):
    if low < high:
        pi = randomPartition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
    return arr 

# 5;希尔排序
def shellSort(arr):
    size = len(arr)
    gap = size // 2 
    while gap > 0:
        for i in range(gap, size):
            temp = arr[i]
            # 每个位置，间隔 gap 进行插入排序
            j = i 
            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap 
            arr[j] = temp 
        gap = gap // 2
    return arr


# 6;归并排序
def merge(left_arr, right_arr):
    arr = []
    while left_arr and right_arr:
        if left_arr[0] < right_arr[0]:
            arr.append(left_arr.pop(0))
        else:
            arr.append(right_arr.pop(0))
    while left_arr:
        arr.append(left_arr.pop(0))
    while right_arr:
        arr.append(right_arr.pop(0))
    return arr 

def mergeSort(arr):
    size = len(arr)
    if size < 2:
        return  arr 
    mid = len(arr) // 2 
    left_arr, right_arr = arr[0:mid], arr[mid:]
    return merge(mergeSort(left_arr), mergeSort(right_arr))