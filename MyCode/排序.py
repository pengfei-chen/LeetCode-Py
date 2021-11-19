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

7; 堆排序

# 调整为大顶堆
def heapify(arr, index, end):
    left = index * 2 + 1
    right = left + 1
    while left <= end:
        # 当前节点为非叶子节点
        max_index = index 
        if arr[left] > arr[max_index]:
            max_index = left 
        if right <= end and arr[right] > arr[max_index]:
            max_index = right 
        if index == max_index:
            #如果不用交换，则说明已经交换结束了
            break 
        arr[index], arr[max_index] = arr[max_index],arr[index]
        # 继续调整子树 
        index = max_index 
        left = index * 2 + 1
        right = left + 1

# 初始化大顶堆
"""
如果原始序列对应的完全二叉树（不一定是堆）的深度为 d，则从 d - 1 层最右侧分支节点（序号为 n/2:向下取整 ）开始，初始时令 i = n/2：向下取整 ，调用堆调整算法。
每调用一次堆调整算法，执行一次 i = i - 1，直到 i == 1 时，再调用一次，就把原始序列调整为了一个初始堆。
"""
def buildMaxHeap(arr):
    size = len(arr)
    # (size - 2) // 2 是最后一个非叶节点， 叶节点不用调整 
    # 巧妙的想法
    for i in range((size-2)//2, -1, -1):
        heapify(arr, i, size-1)
    return arr 

# 升序堆排序，思路如下：
# 1. 先建立大顶堆
# 2. 让堆顶最大元素与最后一个交换，然后调整第一个元素到倒数第二个元素，这一步获取最大值
# 3. 再交换堆顶元素与倒数第二个元素，然后调整第一个元素到倒数第三个元素，这一步获取第二大值
# 4. 以此类推，直到最后一个元素交换之后完毕。
def maxHeapSort(arr):
    buildMaxHeap(arr)
    size = len(arr)
    for i in range(size):
        arr[0], arr[size-i-1] = arr[size-i-1], arr[0]
        heapify(arr, 0, size-i-2)
    return arr



8;计数排序
def countingSort(arr):
    arr_min, arr_max = min(arr), max(arr)
    size = arr_max - arr_min + 1
    counts = [0 for _ in range(size)]

    for num in arr:
        counts[num-arr_min] += 1
    # 对所有的计数累加
    for j in range(1,size):
        counts[j] += counts[j-1]

    res = [0 for _ in range(len(arr))]
    for i in range(len(arr)-1, -1, -1):
        # counts[arr[i] - arr_min] - 1  指定了 arr[i] 在新 res 中的位置
        res[ counts[arr[i] - arr_min] - 1 ] = arr[i]
        counts[ arr[i] -arr_min ] -= 1

    return res 


9; 桶排序
def insertionSort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i
        while j > 0 and arr[j - 1] > temp:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = temp
        
    return arr
    
def bucketSort(arr, bucket_size = 5):
    arr_min, arr_max = min(arr), max(arr)
    bucket_count = (arr_max - arr_min) // bucket_size + 1
    buckets = [[] for _ in range(bucket_count)]
    
    for num in arr:
        buckets[(num - arr_min) // bucket_size].append(num)
        
    res = []
    for bucket in buckets:
        insertionSort(bucket)
        res.extend(bucket)
    
    return res  

10; 基数排序
def radixSort(arr):
    size = len(str(max(arr)))
    buckets = [[] for _ in range(10)]
    
    for i in range(size):
        buckets = [[] for _ in range(10)]
        for num in arr:
            buckets[num // (10**i) % 10].append(num)
        arr.clear()
        for bucket in buckets:
            for num in bucket:
                arr.append(num)
            
    return arr