# 宝物的重量和价值
tr = {(2, 3), (3, 4), (4, 8), (5, 8), (9, 10)}

# 大盗的背包容量
max_weight = 20

# 初始化记忆表格m
# key是（宝物组合，最大重量），value是最大价值
m = {}

def thief(tr, w):
    # 如果宝物组合为空，或者背包容量为0，最大价值为0
    # 设定递归结束的基本条件
    if tr == set() or w == 0:
        m[(tuple(tr), w)] = 0
        return 0
    elif (tuple(tr), w) in m:
        return m[(tuple(tr), w)]
    else:
        # 改变状态向基本结束条件演进，减小问题规模
        # 递归调用
        vmax = 0
        for t in tr:
            # 如果当前宝物的重量小于等于背包容量
            if t[0] <= w:
                v = thief(tr-{t}, w-t[0]) + t[1]
                vmax = max(vmax, v)
        m[(tuple(tr), w)] = vmax
        return vmax

print(thief(tr, max_weight))
