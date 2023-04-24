# 通过将中间结果保存起来，避免重复计算，提高效率
# 递归解法的时间复杂度为O(n^m)，空间复杂度为O(m)

def recDC(coinValueList, change, knownResults):
    minCoins = change
    if change in coinValueList: # 如果找零的钱数正好是硬币的面值，那么就只需要一枚硬币，递归结束的基本条件
        knownResults[change] = 1 # 记录最优解
        return 1
    elif knownResults[change] > 0:
        return knownResults[change] # 查表成功，直接返回
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recDC(coinValueList, change-i, knownResults)
            if numCoins < minCoins:
                minCoins = numCoins
                knownResults[change] = minCoins
    return minCoins

import time

start = time.time()
print(recDC([1, 5, 10, 25], 63, [0]*64)) #64是因为要包含0，用来存储64种情况的最优解
end = time.time()
print("time:", end-start)