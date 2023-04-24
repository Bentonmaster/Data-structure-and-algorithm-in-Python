# 数列求和
def listsum(numList):
    # 最小问题
    if len(numList) == 1:
        return numList[0]
    # 减小规模
    else:
        return numList[0] + listsum(numList[1:])# 调用自身

print(listsum([2,3,4,5,1]))

# 任意进制转换问题
def toStr(n, base):
    convertString = "0123456789ABCDEF"
    # 最小问题
    if n < base:
        return convertString[n]
    # 递归调用
    else:
        return toStr(n//base, base) + convertString[n%base]

print(toStr(1453, 16))

import sys
print(sys.getrecursionlimit()) # 查看递归深度