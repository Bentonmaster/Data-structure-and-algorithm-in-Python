def dpMakeChange(coinValueList, change, minCoins, coinsUsed):
    # 遍历所有需要计算的金额，从 1 到 change
    for cents in range(1, change + 1):
        # 初始时假设所需硬币数量为该金额的面值
        coinCount = cents
        newCoin = 1 # 初始时假设所使用的硬币面值为 1 美分,不进行初始化会报错
        # 遍历所有小于等于该金额的硬币面值
        for j in [c for c in coinValueList if c <= cents]:
            # 如果使用该硬币面值可以得到更少的硬币数量，则更新硬币数量和使用的硬币面值
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
                newCoin = j
        # 将最少硬币数量和使用的硬币面值存入 minCoins 和 coinsUsed 列表
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin
    # 返回达到目标金额所需的最小硬币数量
    return minCoins[change]

def printCoins(coinsUsed, change):
    coin = change
    while coin > 0:
        # 打印出当前所使用的硬币面值
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        # 计算下一个需要打印的硬币面值
        coin = coin - thisCoin

import time

# 定义需要计算的参数
coinValueList = [1, 5, 10, 25, 21]
change = 63
minCoins = [0] * 64 # 初始时所有元素都为 0
coinsUsed = [0] * 64 # 初始时所有元素都为 0

start = time.time()
# 计算达到目标金额所需的最小硬币数量
print(dpMakeChange(coinValueList, change, minCoins, coinsUsed))
end = time.time()
print("time:", end - start)

# 打印出所使用的硬币面值
printCoins(coinsUsed, change)
print("The used coins are:")
print(coinsUsed)

