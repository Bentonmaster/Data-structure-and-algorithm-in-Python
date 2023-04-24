# 传统的归并排序
def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        left = alist[:mid]
        right = alist[mid:]
        mergeSort(left)
        mergeSort(right)

        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                alist[k]=left[i]
                i+=1
            else:
                alist[k]=right[j]
                j+=1
            k+=1
        while i<len(left):
            alist[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            alist[k]=right[j]
            j+=1
            k+=1
    return alist

# 更具有pythonic的归并排序
def mergeSort2(alist):
    # 递归终止条件
    if len(alist)<=1:
        return alist
    # 递归调用
    mid = len(alist)//2
    left = mergeSort2(alist[:mid])
    right = mergeSort2(alist[mid:])

    # 合并
    merged = []
    while left and right:
        merged.append(left.pop(0) if left[0]<right[0] else right.pop(0))
    
    merged.extend(right if right else left)
    return merged

if __name__ == "__main__":
    alist = [54,26,93,17,77,31,44,55,20]
    print(mergeSort(alist))
    print(mergeSort2(alist))
    