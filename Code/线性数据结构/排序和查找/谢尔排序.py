# 以插入排序为基础，对无序表进行“间隔”划分子列表，每个子列表进行插入排序，最后将所有子列表合并
# 由于插入排序的特点，子列表越有序，排序效率越高，因此谢尔排序的效率取决于子列表的划分
# 间隔的选择是谢尔排序的关键，间隔的选择可以是固定的，也可以是动态的
# 谢尔排序能够减少很多原先需要的无效比较，因此谢尔排序的效率比插入排序高
# 谢尔排序的时间复杂度为O(nlogn)，空间复杂度为O(1)

def shellSort(alist):
    # 间隔设定
    sublistcount = len(alist)//2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            # 子列表进行插入排序
            gapInsertionSort(alist, startposition, sublistcount)
        print("After increments of size", sublistcount, "The list is", alist)
        # 间隔减半，直到为0
        sublistcount = sublistcount // 2

def gapInsertionSort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):
        currentvalue = alist[i]
        position = i
        while position >= gap and alist[position-gap] > currentvalue:
            alist[position] = alist[position-gap]
            position = position-gap
        alist[position] = currentvalue

alist = [54,26,93,17,77,31,44,55,20]
shellSort(alist)
print(alist)
