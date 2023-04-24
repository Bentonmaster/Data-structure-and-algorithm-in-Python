import random
# 冒泡排序的时间复杂度为O(n^2)，交换次数为O(n^2)
def bubbleSort(alist):
    for passsum in range(len(alist)-1, 0, -1):
        for i in range (passsum):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]

# alist = [54,26,93,17,77,31,44,55,20]
alist = [i for i in range(10) for j in range(10)]
random.shuffle(alist)
print(alist)
bubbleSort(alist)
print(alist)

# 性能改进，如果某趟比对没有发生任何交换，说明列表已经排好序，可以提前结束算法
# 但是不能改进算法的复杂度

def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                exchanges = True
                alist[i], alist[i+1] = alist[i+1], alist[i]
        passnum = passnum - 1