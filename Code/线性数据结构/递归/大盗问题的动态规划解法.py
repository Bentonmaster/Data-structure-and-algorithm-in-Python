# 宝物的重量和价值
tr = [None, {'w':2, 'v':3}, {'w':3, 'v':4}, {'w':4, 'v':8}, {'w':5, 'v':8}, {'w':9, 'v':10}]

# 大盗的背包容量
max_weight = 20

# 初始化记忆表格m[宝物组合][最大重量]
# key是（宝物组合，最大重量），value是最大价值
m = {(i, w):0 for i in range(len(tr)) for w in range(max_weight+1)}

# 逐个填充表格
for i in range(1, len(tr)):
    for w in range(1, max_weight+1):
        # 如果当前宝物的重量小于等于背包容量
        if tr[i]['w'] <= w:
            m[(i, w)] = max(m[(i-1, w)], m[(i-1, w-tr[i]['w'])] + tr[i]['v'])
        else:
            m[(i, w)] = m[(i-1, w)] # 不能装入背包

print(m[(len(tr)-1, max_weight)])