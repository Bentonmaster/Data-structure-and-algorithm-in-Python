# 相比与冒泡排序，选择排序的交换次数更少，选择排序的时间复杂度为O(n^2)，交换次数为O(n)
def selectionSort(alist):
    for fillslot in range(len(alist)-1, 0, -1):
        positionmax = 0
        for location in range(1, fillslot+1):
            if alist[location] > alist[positionmax]:
                positionmax = location

        alist[fillslot], alist[positionmax] = alist[positionmax], alist[fillslot]

alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)
