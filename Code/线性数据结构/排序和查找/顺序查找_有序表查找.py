# 对于有序表，当数据项存在的时候，对比过程与无序表完全相同
# 不同之处在于，当数据项不存在的时候，对比过程会提前结束

def orderedSequentialSearch(alist, item):
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos = pos + 1
    return found

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(orderedSequentialSearch(testlist, 3))
print(orderedSequentialSearch(testlist, 13))
