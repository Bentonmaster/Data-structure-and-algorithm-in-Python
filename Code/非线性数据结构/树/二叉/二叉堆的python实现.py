class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
    
    # insert方法，上浮法
    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i //2]:
                self.heapList[i], self.heapList[i // 2] = self.heapList[i // 2], self.heapList[i]
            i = i // 2

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize += 1
        self.percUp(self.currentSize)

    # delMin方法，下沉法
    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
            i = mc

    def minChild(self, i):
        # self.currentSize是最后一个元素的下标,表示当前堆的大小
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1
    
    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.percDown(1)
        return retval
    
    # 用无序表生成二叉堆
    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        print(len(self.heapList), i)
        while i > 0:
            #只需要对非叶子节点进行下沉操作
            self.percDown(i)
            i -= 1
        print(self.heapList, i)

    # 利用二叉堆排序
    def heapSort(self):
        alist = []
        while self.currentSize > 0:
            alist.append(self.delMin())
        return alist
    
a = BinHeap()
a.buildHeap([9, 5, 6, 2, 3])
